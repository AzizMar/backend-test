import argparse

from reverse_string import reverse_string
from reverse_words import reverse_words

parser = argparse.ArgumentParser()

if __name__ == '__main__':

    parser.add_argument("-w", dest="reverse_word", help="input word.", type=str)
    parser.add_argument("-r", dest="reverse_string", help="input phrase.", type=str)

    args = parser.parse_args()

    if args.reverse_word:
        reverse_words(args.reverse_word)

    if args.reverse_string:
        reverse_string(args.reverse_string)
