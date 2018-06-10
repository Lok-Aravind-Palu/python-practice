

# class A(object):
#     pass
#
# a = A()
# a() # Here the a object is not callable


class B(object):

    def __init__(self):
        print("This is init funtion")

    def __call__(self):
        print("It is callable function")

b = B()
b()
b.__call__() # We never call the __call__ method like this even though it works
