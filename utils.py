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


