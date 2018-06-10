class A:

    def doit(self):
        print("doit in AAAAAAA")


class B:

    def doit(self):
        print("doit in BBBBBBB")


class C(A, B):
    pass
    # def doit(self):
    #     print("doit in CCCCCCCCC")


def main():
    c = C()
    c.doit()


class AA:

    def doit(self):
        print("doit in AAAAAAA")


class BB:

    def doit(self):
        print("doit in BBBBBBB")


class CC(BB, AA):
    pass
    # def doit(self):
    #     print("doit in CCCCCCCCC")


def mainn():
    c = CC()
    c.doit()


class AAA:

    def doit(self):
        print("doit in AAAAAAA")


class BBB:

    def doit(self):
        print("doit in BBBBBBB")


class CCC(BBB, AAA):

    def doit(self):
        print("doit in CCCCCCCCC")


def mainnn():
    c = CCC()
    c.doit()


if __name__ == '__main__':
    main()
    mainn()
    mainn()
