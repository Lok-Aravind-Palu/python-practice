
tup = (2,3,5,6,7,8,95,2,3,5,4,6)

for i in tup:
    print(i)

tup1 = ("abc","efg","hij")
tup2 = ("klm","nop","qrs")
tupx = tup1 + tup2
print(tupx)

lis = [tup,tup1,tup2]
print(lis)
for i in lis:
    print(i[2])

tupl = (tup,tup1,tup2,tupx)
print(tupl[1][2])
for t in tupl:
    print(t)

list1 = ["sef","grd","Svs","sfs","gsde"]
tpl = tuple(list1)
print(list1)
print(tpl)

# for single element tuple

tep = (234,)
print(type(tep))

# empty tuple
tip = ()
print(type(tip))


# converting string to tuple
st = tuple("strings")
print(type(st))
for i in st:
    print(i)

(a,(b,(c,(d,e)))) = (5,(4,(3,(2,1))))
print(a,b,c,d,e)

def minmax(items):
    return min(items),max(items)

minval,maxval=minmax([2,3,44,5,4,1,4,3,8,99])
print(minval)
print(maxval)




