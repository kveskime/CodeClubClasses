import sys


def charswap(word):
    word = str(word)
    if len(word) >= 2:
        temp = word[1:-1]
        newString = word[-1:] + temp + word[:1]
        return newString

    elif len(word) == 1:
        return word

    elif word == "":
        return word

    else:
        return 0


