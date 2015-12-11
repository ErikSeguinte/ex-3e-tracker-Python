def integer(message, min_value=None, max_value=None):
    """Validates user input is valid integer.
    """
    while True:
        try:
            user_input=int(input(message))
        except ValueError:
           print("Invalid integer. Please try again.")
           continue
        else:
            if (min_value is not None and user_input < min_value) or (max_value is not None and user_input > max_value):
                print("Out of range. Please try again.")
                continue
            else:
                return user_input
