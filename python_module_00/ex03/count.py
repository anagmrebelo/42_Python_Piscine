import sys
import string


def text_analyzer(data=None):
    """This function counts the number of upper characters,
    lower characters, punctuation and spaces in a given text."""
    ponct = string.punctuation

    if (data is None or data == ""):
        data = input("What is the text to analyze?\n")
    if (isinstance(data, str) is False):
        print("AssertionError: argument is not a string")
    else:
        spaces = data.count(" ")
        upper = sum(1 for c in data if c.isupper())
        lower = sum(1 for c in data if c.islower())
        mark = sum(1 for c in data if ponct.find(c) != -1)
        print("The text contains " + str(len(data)) + " character(s):\n")
        print('- ' + str(upper) + ' upper letter(s)')
        print('- ' + str(lower) + ' lower letter(s)')
        print('- ' + str(mark) + ' punctuation mark(s)')
        print('- ' + str(spaces) + ' space(s)')


if __name__ == "__main__":
    n = len(sys.argv)
    if (n > 2):
        print("AssertionError: more than one argument are provided")
    elif (n == 1):
        text_analyzer()
    else:
        text_analyzer(sys.argv[1])
