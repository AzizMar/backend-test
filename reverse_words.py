from utils import get_input


def reverse_words(input_string: str) -> str:
    """
    This function takes a string parameter and reverse it word for word

    :rtype: str
    :param input_string: The string to be reversed
    :return: The reversed string
    """
    words = input_string.split()  # split the string into a list of words
    words = list(reversed(words))  # reverse the list of words
    result = " ".join(words)  # re-combine the reversed list of words into a new string
    print('Reversed Words: ', result)
    return result


if __name__ == '__main__':
    input_str = get_input()
    reverse_words(input_str)
