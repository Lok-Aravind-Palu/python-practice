
x = range(5)
print(x)

for y in range(0,5):
    print(list(range(y,y+5)))

for z in range(20,30):
    if z%2 == 0:
        print(z)

for w in range(0,20,5):
    print(w)



s = [3,2,5,6,67,4,3,5,6]

for d in s:
    print(d)

# wrong way

for g in range(len(s)):
    print(s[g])

# Enumerate

t = [3.45,2,78,90,2.2487]

for r in enumerate(t):
    print(r)

for k,v in enumerate(t):
    print("k = {}, v = {}".format(k,v))


x = enumerate(t)
for z in x:
    print(z)

