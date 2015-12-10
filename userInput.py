def int(message):
    """
    :param message: Validates user input is valid integer.
    :return:
    """
    while True:
        try:
            user_input=int(input(message))
        except ValueError:
           print("Invalid integer. Please try again.")
           continue
        else:
            return user_input
