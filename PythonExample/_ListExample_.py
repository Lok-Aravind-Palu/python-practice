
lis = ["a", "b", "c"]

print(lis[1])

lis.append("d")

print(lis)
print(lis[1:2])
print(lis[-1])

print(len(lis))
print("a" in lis)

del lis[2]
print(lis)

tup = (1,2,3,4,5,6)

dic = {"a":"apple","s":"sandiago","d":"door","f":"fusion"}
print(dic)
print(dic.keys())
print(dic.values())
dic["s"]="sandy"
print(dic["s"])
print(dic.get("l","unknown"))
lod = [{"id":1,"no.":2,"many":3},{"a":"apple","s":"sandiago"},{"second":"bench","castle":"princes"}]
print(lod)