def integer(message, min_value=None, max_value=None, value=None):
    """Validates user input is valid integer.
    :param max_value: max range, inclusive
    :param min_value: minimum range, inclusive
    :param message: input prompt
    :return user_input
    """

    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        else:
            try:
                if (min_value is not None and user_input < min_value) or (
                                max_value is not None and user_input > max_value):
                    raise (ValueError)
            except ValueError:
                print("Out of range. Please try again.")
                continue
            else:
                return user_input


def empty_or_integer(message, min_value=None, max_value=None):
    """Checks if string is empty, otherwise validates an integer"""
    while True:
        user_input = input(message)
        if user_input == "":
            return user_input
        else:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Invalid integer. Please try again.")
                continue
            else:
                try:
                    if (min_value is not None and user_input < min_value) or (
                                    max_value is not None and user_input > max_value):
                        raise (ValueError)
                except ValueError:
                    print("Out of range. Please try again.")
                    continue
                else:
                    return user_input


def boolean(message):
    while True:
        user_input = input(message)

        try:
            user_input = int(user_input)
        except ValueError:
            user_input = str(user_input).lower()

            if user_input == "yes" or user_input == "y":
                return True
            elif user_input == "no" or user_input == "n":
                return False
        else:
            if user_input == 1:
                return True
            elif user_input == 0:
                return False

        print("I'm sorry. I didn't understand that.")
        print("Please use 1, y, or yes for affirmative; or 0, n, or no for negative.")
        continue
