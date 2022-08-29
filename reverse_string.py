from utils import get_input


def reverse_string(input_string: str) -> str:
    """
    This function takes a string parameter and reverse it letter for letter

    :rtype: str
    :param input_string: The string to be reversed.
    :return: The reversed string.
    """
    result = input_string[::-1]
    print('Reversed String: ', result)
    return result


if __name__ == '__main__':
    input_str = get_input()
    reverse_string(input_str)
