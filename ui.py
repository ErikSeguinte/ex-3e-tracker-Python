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
