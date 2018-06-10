# List comprehension:

words = "i have never thought the world is so beautiful unless i realize the beauty remains in our thought not in our sight".split()

length = []
for word in words:
    length.append(len(word))

print(length)

# or

x = [len(word) for word in words]
print(x)

from math import factorial

lis = [factorial(y) for y in range(20)]
print(lis)

lis = [len(str(factorial(y))) for y in range(20)]
print(lis)

# Set Comprehension

se = {len(str(factorial(z))) for z in range(25)}
print(se)


# Dictionary Comprehension

country_capital = {"United Kingdom" : "London","Brazil":"Brazilia","Morrocco":"Rabat","Sweden":"Stockholm"}

capital_and_country = {capital: country for country,capital in country_capital.items()}
print(capital_and_country)



# dictionary ovverride

override = ["hi","hello","forgot","hotel"]

wer = {x[0]:x for x in override}
print(wer)

# prime sqaure divisors

psqd = {x*x : (1,x,x*x) for x in range(50) if x % 2 == 0}
print(psqd)


# iter() and next() functions

iterable = ["jan","feb","march","april","may","june","junly","august","september","october","november","december"]

iterator = iter(iterable)


try:
    i=0
    while i<=12:
        print(next(iterator))

except StopIteration as si:
    print(' ValueError "Out of data" ')



# Generators "yield keyword"


def gen123():
    yield 1
    yield 2
    yield 3


x = gen123()
print(next(x))

print(next(x))

print(next(x))



def gener():
    print("this is first")
    yield 1
    print("this is second")
    yield 2
    print("this is third")
    yield 3
    print("this is last")



x = gener()

print(next(x))

print(next(x))

print(next(x))

try:
    print(next(x))
except StopIteration as si:
   print( 'ValueError("this is the end")' )





