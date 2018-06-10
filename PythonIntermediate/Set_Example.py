
se = {1,2,2,3,6,5,5,8,9}
print(se)

# to convert list to the set
lsi =['a','b','c','d']
print(set(lsi))

#empty set
s = set()
print(type(s))
print(s)

s.add(1)
print(s)

# remove and discard

lsi.remove('a')
se.remove(5)
se.discard(5)
#se.remove(5)
print(se)

q = se.copy()
print(q)

y=q
print(y)

e = set(q)
print(e)

e.update([2,6,5,7,8,9,1,2])
print(e)

