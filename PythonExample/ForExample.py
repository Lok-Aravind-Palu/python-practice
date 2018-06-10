liss = [1, 2, 3, 4, 5, 6, 7, 8]

for x in range(3):
    print(liss[x])

#
y = 0
for index in range(5, 10):
    y += index
    print(y)

#
k = 0
for z in range(4, 10, 2):
    k += z
    print(k)

#
for a in "abrakadabra":
    print(a)

#
for b in liss:
    print(b)

#
for i in liss:
    if i == 3:
        print(i, "cool")
        break
    print("values", i)

#
for j in liss:
    if j==5:
        continue
        print("Baggy")
    print("Bagy",j)