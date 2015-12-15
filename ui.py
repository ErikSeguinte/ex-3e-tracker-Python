import input_validation


class UI:
    """Controls the user interface"""

    def __init__(self, item_list, gambits):
        self.items = item_list

        self.gambit_dict = {}
        self.gambit_names = []

        for gambit in gambits:
            name = gambit[0]
            cost = gambit[1]
            self.gambit_names.append(name)
            self.gambit_dict[name] = cost
        print(self.gambit_dict)
        print(self.gambit_names)

    def print_menu(self):
        """Builds and prints the option menu"""
        menu_item = "{0}) {1}"
        n = 0
        for item in self.items:
            print(menu_item.format(n, item))
            n += 1

    def get_command(self):
        """Gets input from user, converts to proper string."""
        command = input_validation.integer("Enter Command: ", 0, len(self.items) - 1)
        return self.items[command]

    def choose_combatants(self, character_list):
        attacker = input_validation.empty_or_integer("Attacker? Blank = 0: ", 0, len(character_list) - 1)
        defender = input_validation.integer("Defender: ", 0, len(character_list) - 1)

        if attacker == "":
            attacker = 0

        print(character_list[attacker].name + " is attacking " + character_list[defender].name)
        combatants = (attacker, defender)
        return combatants

    def choose_gambit(self):
        attacker = input_validation.integer("Attacker?",0,10) # Still need to validate maximum.
        for i, gambit in enumerate(self.gambit_names):
            print(str(i) + ") " + gambit)
