import ZeltInit
import input_validation



class UI:
    """Controls the user interface"""

    def __init__(self, item_list):
        self.items = item_list

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

    def handle_attack(self, type, number_of_combatants):
        """
        :param type: Type of attack. 0 = Withering, 1 = complex withering, 2 = decisive, 3 = complex decisive, 4 =\
                    gambit, 5 = complex gambit.
        :return:
        """

        if type == 0:
            combatants = self.choose_combatants(number_of_combatants)
            damage = self.get_damage()
            return (combatants, damage)

        elif type == 1:
            pass
        elif type == 2:
            pass
        elif type == 3:
            pass
        elif type == 4:
            pass
        elif type == 5:
            pass

    def get_damage(self):
        damage = input_validation.empty_or_integer("Damage: ")
        return damage

    def get_tricks(self):
        pass
