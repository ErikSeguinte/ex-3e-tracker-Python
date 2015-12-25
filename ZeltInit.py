from random import randint
import time

import input_validation
import user_interface
import re

ITEMS = (
    "Withering Attack",
    "Decisive Attack",
    "Gambits",
    "Other Actions",
    "Add NPCs",
    "Join Battle!",
    "Modify Initiative",
    "Remove from combat",
)
GAMBITS = (
    ("Disarm", 3),
    ("Unhorse", 4),
    ("Distract(3)", 3),
    ("Distract(4)", 4),
    ("Distract(5)", 5),
    ("Grapple", 2),
)

OTHER_ACTIONS = (
    ("Delay", 2),
    ("Disengage", 2),
    ("Withdraw", 10),
    ("Other", 0),
)

global character_list
character_list = []

global player_names
player_names = []

# set up gambits
gambit_dict = {}
gambit_names = []

for gambit in GAMBITS:
    name = gambit[0]
    cost = gambit[1]
    gambit_names.append(name)
    gambit_dict[name] = cost

action_dict = {}
action_names = []

for action in OTHER_ACTIONS:
    name = action[0]
    cost = action[1]
    action_names.append(name)
    action_dict[name] = cost


def debug_print(string):
    """ Prints string. Used in debugging so it can be found easier later.

    :param string: String to be printed
    :return: none
    """
    print(string)


def dice_roller(pool=None, doubles=10):
    """
    :param pool: int: Dice pool to be rolled.
    :param doubles: int: This number or higher earns an additional success.
    :return: number of successes.
    :rtype: int
    """
    if pool is None:
        pool = input_validation.integer("Dice Pool: ")
    successes = 0
    for _i in range(pool):
        d = randint(1, 10)
        if d >= 7:
            successes += 1
        if d >= doubles:
            successes += 1
    return successes


class Character:
    """Class containing all character related variables."""

    def __init__(self):
        self.name = ""
        self.initiative = 0
        self.inert_initiative = False
        self.crash_state = False
        self.crash_counter = 0  # Number of turns in crash
        self.crash_return_counter = 0  # Number of turns after returning from crash
        self.has_gone = False
        self.join_battle_pool = 0
        self.shift_target = None  # Character who crashed this character, for init shift.
        self.recently_crashed = False

    def set_name(self):
        self.name = input("Name: ")

    def set_init(self):  # Join Battle roll.
        if self.join_battle_pool is None:
            self.initiative = input_validation.integer("Join Battle roll for " + self.name + ": ") + 3
        else:
            self.initiative = self.join_battle() + 3

    def set_has_gone(self):
        self.has_gone = True

    def __str__(self):
        return str(self.name).rstrip()

    def __repr__(self):
        return str(self.name).rstrip()

    def join_battle(self):
        self.initiative = dice_roller(self.join_battle_pool) + 3

    def get_values(self):
        yield self.name
        yield self.initiative
        yield self.inert_initiative
        yield self.crash_state
        yield self.crash_counter
        yield self.crash_return_counter
        yield self.has_gone
        yield self.join_battle_pool
        yield self.shift_target
        yield self.recently_crashed


    def set_values(self, values):
        new_values = value_generator(values)
        self.name = next(new_values)
        self.initiative = next(new_values)
        self.inert_initiative = next(new_values)
        self.crash_state = next(new_values)
        self.crash_counter = next(new_values)
        self.crash_return_counter = next(new_values)
        self.has_gone = next(new_values)
        self.join_battle_pool = next(new_values)
        self.shift_target = next(new_values)
        self.recently_crashed = next(new_values)


def clear_screen():
    """Prints a bunch of new lines to clear the screen."""
    for i in range(10):
        print("")


def add_players(f="Players.txt"):
    """Add player names from an external file."""

    global character_list
    with open(f, encoding='utf-8') as player_file:
        for a_line in player_file:
            character = Character()
            name = a_line.rstrip()
            character.name = name
            character_list.append(character)
            player_names.append(name)


def add_npcs(f="Players.txt"):
    """Add player names from an external file."""

    global character_list
    with open(f, encoding='utf-8') as player_file:
        for a_line in player_file:
            name = None
            jb = None
            inert = None
            try:
                name, jb, inert = a_line.split(",")
            except ValueError:
                try:
                    name, jb = a_line.split(",")
                except ValueError:
                    try:
                        name = a_line
                    except ValueError:
                        break

            character = Character()
            print(name)
            character.name = name.strip()
            if jb:
                try:
                    jb_int = int(jb.strip())

                except ValueError:
                    pass
                else:
                    if jb_int > 0:
                        character.join_battle_pool = jb_int
            if inert:
                inert = str(inert).lower().strip()
                if inert == "true" or inert == "1":
                    character.inert_initiative = True
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
                name=str(char),
                init=str(char.initiative),
                crash=char.crash_state,
                id=str(n),
                gone=char.has_gone))
        n += 1


def sort_table():
    global character_list
    character_list = sorted(character_list, key=lambda character: character.initiative, reverse=True)
    character_list = sorted(character_list, key=lambda character: character.has_gone)


def add_npc(name, inert, join_battle, initiative):
    global character_list
    new_character = Character()
    new_character.name = name
    new_character.join_battle_pool = join_battle
    new_character.inert_initiative = inert
    new_character.initiative = initiative
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


def handle_withering(combatants, damage, trick=(False, 0, 0), rout=0):
    global character_list
    attacker_index, defender_index = combatants
    attacker, defender = character_list[attacker_index], character_list[defender_index]

    # if __name__ == '__main__':
    # debug_print(str(combata/nts, damage, trick))

    # Reset Crash Counter at the beginning of the 4th turn if survives
    reset_crash_check(attacker)

    handle_tricks(combatants, *trick)

    attacker.has_gone = True
    if not defender.inert_initiative:
        if damage != 0:
            shifting = False
            if check_for_crash(defender_index, damage):
                if attacker.shift_target is defender:  # Initiative Shift!
                    shifting = True
                attacker.initiative += 5
                defender.crash_state = True
                defender.shift_target = attacker

            # Successful Attack
            attacker.initiative += damage + 1
            if shifting:
                attacker.has_gone = False
                if attacker.initiative < 3:
                    attacker.initiative = 3
                attacker.initiative += dice_roller(attacker.join_battle_pool)

            defender.initiative -= damage
            if attacker.initiative > 0:
                if attacker.crash_state:
                    attacker.recently_crashed = True
                attacker.crash_state = False
                attacker.crash_counter = 0
                attacker.shift_target = None
            else:
                attacker.crash_state = True
                attacker.recently_crashed = False
    else:
        bonus = (rout * 5) + 1
        attacker.initiative += bonus

    if attacker.crash_state:
        attacker.crash_counter += 1

    if check_for_end_of_round():
        reset_has_gone()


def check_for_end_of_round():
    global character_list
    for character in character_list:
        if not character.has_gone:
            return False
    return True


def reset_has_gone():
    global character_list

    for character in character_list:
        if character.crash_return_counter >= 1:
            character.crash_return_counter = 0
            character.recently_crashed = False
        if character.recently_crashed:
            character.crash_return_counter += 1
        character.has_gone = False


def name_generator():
    names = ("Arnold",
             "Billy",
             "Carol",
             "David",
             "Earl")
    for name in names:
        yield name


def value_generator(values):
    print("Generating Values")
    print(str(values))
    for value in values:
        print(value)
        yield value


def set_up_test():
    global character_list
    character_list = [Character(), Character(), Character(), Character(), Character(), ]
    i = 0
    generator = name_generator()
    for character in character_list:
        character.name = next(generator)
        character.initiative = i
        if i % 4 == 0:
            character.initiative *= -1
        character.join_battle_pool = i + 1

        character.has_gone = ((i % 2) == 1)
        if character.initiative <= 0:
            character.crash_state = True
        i += 1
    sort_table()


def handle_tricks(combatants, trick_status=False, att_trick=0, def_trick=0):
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


def handle_decisive(combatants, success, trick=(False, 0, 0), rout=0):
    attacker = combatants[0]

    a = character_list[attacker]

    reset_crash_check(a)
    handle_tricks(combatants, *trick)

    if success:
        a.initiative = (rout * 5) + 3
    else:
        if a.initiative <= 10:
            a.initiative -= 2
        else:
            a.initiative -= 3
    a.has_gone = True


def remove_from_combat(character_index):
    global character_list
    print("Removing:")
    print(character_list[character_index])
    del character_list[character_index]


def handle_gambits(combatants, success, gambit, trick=(False, 0, 0), ):
    attacker = character_list[combatants[0]]
    defender = character_list[combatants[1]]
    cost = gambit_dict[gambit] + 1

    reset_crash_check(attacker)
    handle_tricks(combatants, *trick)

    if check_for_crash(combatants[0], cost):
        attacker.initiative -= 5
        defender.initiative += 5

    if success:
        attacker.initiative -= cost
        if re.search(r"Distract", gambit):
            defender.initiative += cost - 1
            print("Distracted!")
    else:
        if attacker.initiative <= 10:
            attacker.initiative -= 2
        else:
            attacker.initiative -= 3

    attacker.has_gone = True


def reset_crash_check(attacker):
    if attacker.crash_counter >= 3:
        attacker.crash_counter = 0
        attacker.crash_state = False
        attacker.initiative = 3


def remove_character(char_index):
    return character_list.pop(char_index)


def main():
    global character_list

    add_players()
    ui = user_interface.UI(ITEMS, GAMBITS)

    while True:
        clear_screen()
        sort_table()
        print_table()
        print("")
        ui.print_menu()
        number_of_combatants = len(character_list)
        command = ui.get_command()
        if command == "Withering Attack":
            print("    " + command)
            handle_withering(*ui.attack_interface(0, number_of_combatants))

        elif command == "Decisive Attack":
            print("    " + command)
            handle_decisive(*ui.attack_interface(2, number_of_combatants))
        elif command == "Join Battle!":
            print("    " + command)
            for c in character_list:
                c.set_init()
        elif command == "Add NPCs":
            print("    " + "Adding NPCs")
            max_loop = input_validation.integer("How many NPCs to add? ")
            print("Enter an empty line to quit.")
            for _i in range(max_loop):
                name = input("New name: ")

                # Empty strings are false.
                if not name:
                    break
        elif command == "Other Actions":
            pass
        elif command == "Gambits":
            handle_gambits(*ui.attack_interface(4, number_of_combatants))

        elif command == "Modify Initiative":
            pass


def handle_other_actions(character_index, cost, delay=False):
    character = character_list[character_index]
    character.initiative -= cost

    if not delay:
        character.has_gone = True


def reset_combat():
    global character_list
    global player_names
    character_list[:] = [character for character in character_list if character.name in player_names]


if __name__ == '__main__':
    main()
