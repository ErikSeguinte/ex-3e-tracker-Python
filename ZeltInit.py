from random import randint

import input_validation
from ui import UI

ITEMS = (
    "Withering Attack",
    "Decisive Attack",
    "Add NPCs",
    "Join Battle!"
)

global character_list


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


def choose_combatants():
    global character_list
    attacker = input_validation.empty_or_integer("Attacker? Blank = 0: ", 0, len(character_list))
    defender = input_validation.integer("Defender?", 0, len(character_list))

    if attacker == "":
        attacker = 0

    print(character_list[attacker].name + " is attacking " + character_list[defender].name)
    combatants = (attacker, defender)
    return combatants


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


def handle_withering():
    combatants = choose_combatants()
    damage = input_validation.empty_or_integer("Damage: ")

    if damage != 0:
        # Check for Crash
        if check_for_crash(combatants, damage):
            pass

        # Successful Attack
        combatants[0].initiative += damage + 1
        combatants[1].initiative -= damage
    combatants[0].has_gone = True


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


if __name__ == '__main__':
    character_list = []
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


        elif command is "Decisive Attack":
            print("    " + command)
            combatants = choose_combatants()
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
            i = 0
            print("Enter an empty line to quit.")
            for i in range(max_loop):
                name = input("New name: ")

                # Empty strings are false.
                if not name:
                    break
