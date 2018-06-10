
class Animal(object):

    def ebility(self):
        print("can walk and crawl and run ...")

    def inebility(self):
        print("Illiterate")


class Human(Animal):

    def ebility(self):
        print("can walk and run")


class Snake(Animal):

    def ebility(self):
        print("can crawl")


def main():

    a = Animal()
    a.ebility()

    b = Human()
    b.ebility()
    b.inebility()


if __name__ == '__main__':
    main()
