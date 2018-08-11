
store = []


def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]
    store.append(last_letter)
    print(last_letter)
    return sorted(strings, key=last_letter)


sort_by_last_letter(['ghi', 'def', 'abc'])


# First Class Functions
def outer():
    def inner():
        print('inner')
    return inner


o = outer()
o()


def function_Call():
    class InnerClass:
        def __init__(self):
            print('Inner class')

        def  call_me(self):
            print("you called me")

    return InnerClass


f = function_Call()
f().call_me()
