import sys
from typing import Optional


def get_input() -> Optional[str]:
    """
    a helper function that checks if command line argument exists and returns its value

    :return: command line argument value
    """
    if len(sys.argv) <= 1 or not sys.argv[1]:
        print("ERROR: Missing string argument.")
        exit()

    return sys.argv[1]


def get_file_content(filename: str) -> Optional[str]:
    """
    a helper function that checks if a file exists and returns its content

    :rtype: str
    :param filename: name of file that contains the input string
    :return: file content
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("ERROR: File does not exist!")
        exit()
