import sys


def readf(path):
    if type(path) != str:
        sys.exit(15)
    with open(path, "r+", encoding="utf8") as file:
        list01 = []
        for text in file.readlines():
            list01.append(text)
    return list01


def asum(a, b):
    return a + b

