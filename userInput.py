def integer(message):
    """Validates user input is valid integer.
    :param message: input prompt
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
