import sys
import os


def recursive(number=2):
    if type(number) != int:
        sys.exit(2)
    def r(number):
        if number <= 0:
            return 1
        return number * r(number - 1)
    return r(number)


def openfile(path):
    if type(path) != str:
        sys.exit(3)
    def o(path):
        text = []
        with open(path, "r+", encoding="utf8") as file:
            for line in file.readlines():
                text.append(line)
            return text
    return o(path)


class Doc:
    def __init__(self, name, size, permission, kind, path):
        self.name = name
        self.size = size
        self.permission = permission
        self.kind = kind
        self.path = path

    def getSize(self):
        os.system("du -sh {}/{}".format(self.path, self.name))


















