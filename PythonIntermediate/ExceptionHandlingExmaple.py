import sys
from math import log

def convert(s):
    try:
        return int(s)
    except (TypeError,KeyError,ValueError) as e:
        print("Conversion Error: {}"\
              .format(str(e)),file =sys.stderr)
        return -1


print(convert("123"))
print(convert("Elephant"))
print(convert([2,5,6,8,9]))

# we can have more than one exception

def cal_square(y):

    try:
        return (y*y)
    except TypeError as t:
        print("put some integer",t)
    except KeyError as k:
        print("put some integer",k)
    finally:
        print("Exection is done")


print(cal_square(convert("56")))

def log_math(v):
    x = convert(v)
    print(log(x))

log_math("63")

# Raise exception

def con_dict(b):

    try:
        x = dict(b)
        print(x)
    except (KeyError,ValueError,TypeError) as e:
        print(file=sys.stderr)
        #raise

con_dict([1,2,3])



# Raise

def sqrt_func(q):

    if q < 0:
        raise ValueError("Cannot compute the negative numbers {}".format(q))


    guess = q
    i = 0
    while guess*guess != guess and  i<20:
        guess = (guess+q/guess)/2.0
        i +=1

    return guess

def sqrt_main():

    try:

        sqrt_func(9)
        sqrt_func(3)
        sqrt_func(-1)

    except ValueError as v:
        print(v,file=sys.stderr)

sqrt_main()


# OS error

import os

p = 'E:\Timesheets'

if os.path.exists(p):
    print("Yes exists")
else:
    print("Does not contain".format(p))

 #or the best way is

try:
    print("path presents")
except OSError as os:
    print("does not contain this file".format(p),file=sys.stderr)

