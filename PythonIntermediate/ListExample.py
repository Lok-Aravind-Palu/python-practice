
s = "this is how the world is so happy "
fullsize = s[:]
print(s[:].split(" "))
print(fullsize)

if fullsize is s:
    print(fullsize is s)
elif fullsize == s:
    print(fullsize == s)
else:
    print("nothing")

v = list(s)
print(v)

list1 = [[1,2,3,4],[5,6,4,8,4],[8,5,6,6,9,1]]
print(list1[1])


# Shallow copies
a = [[1,2],[3,4]]
b = a[:]


print(a is b)
print(a == b)
print(a[0] is b[0])
print(a[0] == b[0])

d = a*3
print(d)
print("="*10)


print((3,5)*2)


lis1 = [2,5,9,6,3,5,6,8]
del lis1[2]
print(lis1)

lis1.remove(5)
print(lis1)

del lis1[lis1.index(8)]
print(lis1)

a = "i accidentally the whole universe".split()
print(a)

a.insert(2,"destroyed")
a=" ".join(a)
print(a)

# extend method
m = [2,5,4,8]
k = [3,5,63,9,5]

k += [15,14,16]
print(k)

k.extend([15,5,6,3,2,4])
print(k)


tuples =(5,6,2,5,6,2)
print(len(tuples))

# Revese order

rev = [112,55,3,655,2,56,452,545]
rev.reverse()
print(rev)

rev.sort()
print(rev)

rev.sort(reverse = True)
print(rev)
# Sort order

sor = ["the  ","apple ","an ","a ","doctor "," have "]

sor.sort(key = len)
print(sor)

# sorted

k = [5,2,66,254,6,5,3,1,4,888,3,52,65]
s = sorted(k)
print(k)
print(s)

# reversed

q = [7,8,2,5,6,8,4,25,5,56,8]

z = reversed(q)
print(z)
print(list(z))
print(q)