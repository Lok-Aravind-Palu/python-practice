import sys
sys.path.append("..")

from ..file_1 import FileOne
from .file_2 import FileTwo


class FileThree:

    def __init__(self):
        self.file_1 = FileOne()
        self.file_2 = FileTwo()

    def sample(self):
        print("This is from file_3")

    def printint(self):
        self.sample()
        self.file_1.sample()
        self.file_2.sample()


if __name__ == '__main__':
    f3 = FileThree()
    f3.printint()
