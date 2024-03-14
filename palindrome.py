def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    value = value.replace(" ", "").lower()
    if value == value[::-1]:
        return True
    else:
        return False

