from random import randint

import input_validation
from ui import UI

ITEMS = (
    "Withering Attack",
    "Decisive Attack",
    "Gambits",
    "Other Actions",
    "Add NPCs",
    "Join Battle!",
    "Modify Initiative",
)
GAMBITS = (
    ("Disarm", 3),
    ("Unhorse", 4),
    ("Distract", 3),
    ("Distract", 4),
    ("Distract", 5),
    ("Grapple", 2),
)

character_list = []


def dice_roller(pool=None):
    if pool is None:
        pool = input_validation.integer("Dice Pool: ")
    successes = 0
    i = 0
    while i < pool:
        d = randint(1, 10)
        if d >= 7:
            successes += 1
        if d == 10:
            successes += 1
        i += 1
    return successes


class Character:
    """Class containing all character related variables."""

    def __init__(self):
        self.name = ""
        self.initiative = 0
        self.inert_initiative = False
        self.crash_state = False
        self.crash_counter = 0
        self.shift_target = ""
        self.has_gone = False
        self.join_battle = None

    def set_name(self):
        self.name = input("Name: ")

    def set_init(self, successes=None):
        if successes is None:
            self.initiative = input_validation.integer("Join Battle for " + self.name + ": ") + 3
        else:
            self.initiative = successes + 3

    def set_has_gone(self):
        self.has_gone = True


def clear_screen():
    """Prints a bunch of new lines to clear the screen."""
    for i in range(10):
        print("")


def add_players():
    """Add player names from an external file."""
    global character_list
    with open('Players.txt', encoding='utf-8') as player_file:
        for a_line in player_file:
            character = Character()
            character.name = a_line.rstrip()
            character_list.append(character)


def print_table():
    """Prints characters and initiative status, in order."""
    global character_list

    n = 0
    fmt = "({id:>3}){name:>15} | {init:^5} | {crash:^5} | {gone:^5}"
    print(fmt.format(
            name="Name",
            init="init",
            crash="crash",
            id="id",
            gone="gone"))
    print("===========================================")
    for char in character_list:
        print(fmt.format(
                name=char.name,
                init=str(char.initiative),
                crash=char.crash_state,
                id=str(n),
                gone=char.has_gone))
        n += 1


def sort_table():
    global character_list
    character_list = sorted(character_list, key=lambda character: character.initiative, reverse=True)
    character_list = sorted(character_list, key=lambda character: character.has_gone)


def add_npc(name):
    global character_list
    new_character = Character()
    new_character.name = name
    join_battle = input_validation.integer("Join Battle Dice Pool: ")
    new_character.join_battle = join_battle
    character_list.append(new_character)


def add_new_character():
    """

    :rtype: object
    """
    new_character = Character()
    new_character.set_name()
    new_character.set_init()
    return new_character


def check_for_crash(defender, init_damage):
    """Checks if this attack would cause defender to crash

    :param init_damage:     Damage taken in this attack
    :param defender:        index of defender
    :return  bool           True if attack would crash defender
    """
    global character_list
    init = character_list[defender].initiative
    new_init = init - init_damage
    if init > 0 >= new_init:
        # Crash!
        return True
    else:
        return False


def handle_withering(combatants, damage, trick):
    global character_list
    attacker = character_list[combatants[0]]
    defender = character_list[combatants[1]]

    handle_tricks(combatants, *trick)

    if damage != 0:
        # Check for Crash
        if check_for_crash(combatants[1], damage):
            attacker.initiative += 5
            defender.crash_state = True

        # Successful Attack
        attacker.initiative += damage + 1
        defender.initiative -= damage
        if attacker.initiative > 0:
            attacker.crash_state = False
            attacker.crash_counter = 0
        else:
            attacker.crash_state = True
    attacker.has_gone = True

    if check_for_end_of_round():
        reset_has_gone()

        # character_list[combatants[0]] = attacker
        # character_list[combatants[1]] = defender


def handle_decisive(attacker, success):
    global character_list
    character = character_list[attacker]
    if success is True:
        character.initiative = 3
    else:
        if character.initiative >= 11:
            character.initiative -= 3
        else:
            character.initiative -= 2
    character.has_gone = True


def check_for_end_of_round():
    global character_list
    for character in character_list:
        if not character.has_gone:
            return False
    return True


def reset_has_gone():
    global character_list

    for character in character_list:
        character.has_gone = False


def name_generator():
    names = ("Arnold",
             "Billy",
             "Carol",
             "David",
             "Earl")
    for name in names:
        yield name


def set_up_test():
    global character_list
    character_list = [Character(), Character(), Character(), Character(), Character(), ]
    i = 0
    generater = name_generator()
    for character in character_list:
        character.name = next(generater)
        character.initiative = i
        if i % 4 == 0:
            character.initiative *= -1
        character.join_battle = i
        character.has_gone = i % 2
        if character.initiative <= 0:
            character.crash_state = True
        i += 1
    sort_table()


def handle_tricks(combatants, trick_status, att_trick, def_trick):
    global character_list
    attacker = character_list[combatants[0]]
    defender = character_list[combatants[1]]
    if trick_status:
        if att_trick < 0:
            if check_for_crash(combatants[0], att_trick * -1):
                attacker.initiative -= 5
                attacker.crash_state = True
            attacker.initiative += att_trick

    if def_trick < 0:
        if check_for_crash(combatants[1], def_trick * -1):
            defender.initiative -= 5
            defender.crash_state = True
            attacker.initiative += 5
        defender.initiative += def_trick


def main():
    global character_list

    add_players()
    ui = UI(ITEMS)
    while True:
        clear_screen()
        sort_table()
        print_table()
        print("")
        ui.print_menu()
        command = ui.get_command()
        if command is "Withering Attack":
            print("    " + command)
            combatants = ui.choose_combatants()
            damage = input_validation.empty_or_integer("Damage: ")
            handle_withering(combatants, damage, (False, 0, 0))

        elif command is "Decisive Attack":
            print("    " + command)
            combatants = ui.choose_combatants()
        elif command is "Join Battle!":
            print("    " + command)
            for c in character_list:
                if c.join_battle is None:
                    c.set_init()
                else:
                    c.initiative = dice_roller(c.join_battle)
        elif command is "Add NPCs":
            print("    " + "Adding NPCs")
            max_loop = input_validation.integer("How many NPCs to add? ")
            print("Enter an empty line to quit.")
            for _i in range(max_loop):
                name = input("New name: ")

                # Empty strings are false.
                if not name:
                    break
        elif command is "Other Actions":
            pass
        elif command is "Gambits":
            pass
        elif command is "Modify Initiative":
            pass


if __name__ == '__main__':
    main()
