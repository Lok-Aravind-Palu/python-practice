from math import sqrt


def primeNumber(x):
    if x < 2:
        return False
    for z in range(2, int(sqrt(x))+1):
        if x%z == 0:
            return False
    return True


print(primeNumber(2))
print(primeNumber(0))
print(primeNumber(17))
print(primeNumber(256))


lis = [x for x in range(101) if primeNumber(x)]
print(lis)

lis = [x for x in range(101)]
print(lis)
