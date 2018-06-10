

a = 5
print(id(a))

b = 5

print(id(b))

print(a is b)


# lists

x = [1,2,3]
s = x

print(x is s)
print(x == s)

s[1] = 5
print(x)
print(s)
# list with reference --- (is keyword check the reference of the object)

l = [1,7,11]
b = [1,7,11]

print(l==b)
print(l is b)


#

m = [7,15,24]
def modefy(k):
    k.append(28)
    print("k = " , k)

modefy(m)
print("m = ",m)

#

f = [12,65,78]

def model(g):
    g = [2,33,45]
    print("g = ", g)

model(f)
print("f = ",f)

#
g = [34,45,65]

def t(d):
    return d

e = t(g)
print(g is e)

#

def substitute(message, distribute = '-'):
    string = distribute * len(message)
    print(string)
    print(message)
    print(string)

substitute("hello world")
substitute("pendrive","*")
substitute("blackhole",distribute = "*")

#Default Argument

import time

def show_time(arg = time.ctime()):
    print(arg)


show_time()
show_time()

#

def show_spam(menu=[]):
    menu.append("spam")
    print(menu)

breakfast = ["honey","oats"]
lunch = ["rice","curry"]

show_spam(breakfast)
show_spam(lunch)

show_spam()
show_spam()
show_spam()

# Global Variable

count = 0

def show_count():
    print("count = ", count)

def put_count(c):
    count = c

put_count(5)
show_count()

con = 0
def show_con():
    print("con = ", con)


def put_con(c):
    global con
    con = c

put_con(10)
show_con()