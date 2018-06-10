from abc import ABC, abstractmethod


class ExampleAbstractMethod(ABC):

    @abstractmethod
    def move(self):
        print("Can walk and run....")


class ExampleImportAbstractMethod(ExampleAbstractMethod):

    def move(self):
        print("can crawl")


def main():

    a = ExampleImportAbstractMethod()
    a.move()


if __name__ == '__main__':
    main()
