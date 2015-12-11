import userInput


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
        self.initiative = userInput.integer("Join Battle: ")

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
    """Prints characterss and initiative status, in order."""
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

def print_menu():
    menu_item = "{0}) {1}"
    items = (
        "Withering Attack",
        "Decisive Attack",
        "Add NPCs",
        "Join Battle!"
    )
    n=0
    for item in items:
        print(menu_item.format(n, item))
        n+=1

print("Hello World")
clear_screen()
character_list = add_players()
while True:
    clear_screen()
    print_table(sort_table(character_list))
    print("")
    command = input()
print_menu()
