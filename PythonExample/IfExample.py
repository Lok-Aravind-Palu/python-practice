a = 5
b = 10

if (a > b):
    print("a");
else:
    print("b")

#
if (a > b):
    print("a")
elif (b > a):
    print("b")
else:
    print("a&b")

#
if a:
    print("Truthy")
else:
    print("Falsy")

#

c = True
d = False

if c:
    print("Ture")
elif d:
    print("False")
else:
    print("T&F")

#
if c is not True:
    print("c")
elif d is not True:
    print("d")
else:
    print("e")

#
str = "comcast"

if "st" in str:
    print("yes it has")

#
if "ss" not in str:
    print(str)

#

if not str:
    print("not in it")
else:
    print("yes it is falsy")

#
ptr = None

if not ptr:
    print("not in it")
else:
    print("yes it is falsy")

#

if "cat" in "caterpiller":
    print("Tes it is there")
else:
    print("Not there")

#
c = "apple"
if ("app" in c):
    print("yes it is there")

#
f = "string"
if type(f) == str:
    print("It is a string")
else:
    print("Not a string")

#

ceaser = ''

if ceaser:
    print("it works")
elif not ceaser:
    print("it really works")
else:
    print("it should")

#

number = 3
python_course = True

if (number == 3 and python_course):
    print("This will execute")
else:
    print("This won't execute")

#
if (number == 17 or python_course):
    print("This will only execute")
else:
    print("This will also execute")

#

var = "better" if a > b else "smaller"
print(var)
