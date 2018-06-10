class CallableExample(object):
    def __init__(self):
        self.lam = lambda x: x**2

    def __call__(self):
        print("called")

    def whether_method(self):
        print("yes")

    def is_even(self, x):
        return x % 2 == 0


if __name__ == '__main__':
    c = CallableExample()
    print(callable(c.whether_method))
    print(callable(c.is_even))
    print(callable(c))
    print(callable(c.lam))
    print(callable(list))
    print(callable(list.append))
    print(callable("This is not callable"))
