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

    def choose_combatants(self, number_of_combatants):
        attacker = input_validation.empty_or_integer("Attacker? Blank = 0: ", 0, number_of_combatants - 1)
        defender = input_validation.integer("Defender: ", 0, number_of_combatants - 1)

        if attacker == "":
            attacker = 0

        combatants = (attacker, defender)
        return combatants

    def attack_interface(self, attack_type, number_of_combatants):
        """
        :param number_of_combatants:
        :param attack_type: Type of attack. 0 = Withering, 1 = complex withering, 2 = decisive, 3 = complex decisive, 4 =\
                    gambit, 5 = complex gambit.
        :return:
        """
        combatants = self.choose_combatants(number_of_combatants)
        if attack_type == 0:
            damage = self.get_damage()
            return combatants, damage

        elif attack_type == 1:
            damage = self.get_damage()
            trick = self.get_tricks()
            return combatants, damage, trick
        elif attack_type == 2:
            pass
        elif attack_type == 3:
            pass
        elif attack_type == 4:
            gambit, cost = self.get_gambit()
            return combatants, gambit, cost
        elif attack_type == 5:
            pass

    def get_damage(self):
        damage = input_validation.empty_or_integer("Damage: ")
        return damage

    def get_tricks(self):
        off_trick = input_validation.empty_or_integer("Defensive Init Modification: ")
        def_trick = input_validation.empty_or_integer("Defensive Init Modification: ")

        if off_trick == "":
            off_trick = 0
        if def_trick == "":
            def_trick = 0

        if off_trick == 0 and def_trick == 0:
            return None
        else:
            trick = (True, off_trick, def_trick)
            return trick

    def get_gambit(self):
        print("")
        for i, gambit in enumerate(self.gambit_names):
            cost = self.gambit_dict[gambit]
            print("    " + str(i) + ") " + gambit + ", " + str(cost) + "i")

        gambit_number = input_validation.integer("Choose Gambit: ")
        gambit_name = self.gambit_names[gambit_number]
        return gambit_name, self.gambit_dict[gambit_name]
