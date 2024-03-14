def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    #remove spaces, pop off the end and reconfigure to a new string? compare
    # new and old strings return true if same, else false
    value = value.replace(" ", "")
    if value == reversed(value):
        return True
    else:
        False
