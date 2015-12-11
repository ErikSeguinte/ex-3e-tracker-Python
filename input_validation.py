def integer(message, min_value=None, max_value=None):
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
