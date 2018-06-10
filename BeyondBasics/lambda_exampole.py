
class LambdaExample(object):

    def __init__(self):
        self.lam = lambda x: 3 * x + 1
        self.scientist = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()

    def call_lambda(self):
        y = self.lam(5)
        print(y)

    def call_full_name(self, fn, ln):
        u = self.scientist(fn, ln)
        print(u)

    def quadratic_expressions(self, a, b, c):
        return lambda x: a*x**2+b*x+c


if __name__ == '__main__':
    l = LambdaExample()
    l.call_lambda()
    z =l.quadratic_expressions(5, -2, 3)
    print(z(0))
    print(z(3))
    print(z(9))
    l.call_full_name("  aravind", "PALUVADI   ")
