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
        self.has_gone=False

    def SetName(self):
        self.name = input("Name: ")

    def set_init(self):
        self.initiative = userInput.integer("Join Battle: ")


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

def print_table(list):
    n=0
    fmt = "({id:>3}){name:>15} | {init:^5} | {crash:^5}"
    print(fmt.format(
        name="Name",
        init="init",
        crash="crash",
        id="id"))
    print("------------------------------------")
    for char in list:
        print(fmt.format(
        name=char.name,
        init=str(char.initiative),
        crash=char.crash_state,
        id=str(n)))
        n += 1

def sort_table(list):
    return sorted(list,key=lambda character:character.initiative,reverse=True)




character_list = []
print("Hello World")
clear_screen()
character_list.append(add_new_character())
character_list.append(add_new_character())
character_list.append(add_new_character())
#print(character_list[0].name + " " + str(character_list[0].initiative))
print_table(sort_table(character_list))
