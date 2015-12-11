from random import randint
import input_validation
from ui import UI

ITEMS = (
    "Withering Attack",
    "Decisive Attack",
    "Add NPCs",
    "Join Battle!"
)


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

    def SetName(self):
        self.name = input("Name: ")

    def set_init(self):
        self.initiative = input_validation.integer("Join Battle: ")

    def set_has_gone(self):
        self.has_gone = True


def clear_screen():
    """Prints a bunch of new lines to clear the screen."""
    for i in range(24):
        print("")


def add_new_character():
    """

    :rtype: object
    """
    new_character = Character()
    new_character.SetName()
    new_character.set_init()
    return new_character


def add_players():
    """Add player names from an external file."""
    character_list = []
    with open('Players.txt', encoding='utf-8') as player_file:
        for a_line in player_file:
            character = Character()
            character.name = a_line.rstrip()
            character_list.append(character)

    return character_list


def print_table(list):
    """Prints characters and initiative status, in order."""
    n = 0
    fmt = "({id:>3}){name:>15} | {init:^5} | {crash:^5} | {gone:^5}"
    print(fmt.format(
            name="Name",
            init="init",
            crash="crash",
            id="id",
            gone="gone"))
    print("===========================================")
    for char in list:
        print(fmt.format(
                name=char.name,
                init=str(char.initiative),
                crash=char.crash_state,
                id=str(n),
                gone=char.has_gone))
        n += 1


def sort_table(list):
    sorted_list = sorted(list, key=lambda character: character.initiative, reverse=True)
    return sorted(sorted_list, key=lambda character: character.has_gone)


def dice_roller():
    pool = input_validation.integer("Dice Pool: ")
    successes = 0
    i = 0
    while i < pool:
        d = randint(1, 10)
        print(d)
        if d >= 7:
            successes += 1
        if d == 10:
            successes += 1
        i += 1
    return successes


print("Hello World")
clear_screen()
character_list = add_players()
ui = UI(ITEMS)
while True:
    clear_screen()
    print_table(sort_table(character_list))
    print("")
    ui.print_menu()
    command = ui.get_command()
    if command is "Withering Attack":
        print(command)
    print(str(dice_roller()) + " successes!")
