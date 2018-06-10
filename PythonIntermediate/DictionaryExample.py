
lis = [('alice',32),('john',35),('jenny',34)]
print(dict(lis))

alphabets = dict(a = 'android',b = 'bamboo',c = 'cortana',d = 'Dell',e = 'excel')
print(alphabets)

words = alphabets.copy()
print(words)

for keys in words:
    print(keys)

for key in words.keys():
    print(key)

for val in words.values():
    print(val)

words.update({'a':'apple'})
print(words)

for key,value in words.items():
    print("key -> {k}, Value -> {v}".format(k=key,v=value))

if 'a' in words:
    print(True)
else:
    print(False)

if 'apple' in words.values():
    print(True)
else:
    print(False)

if 'apple' in words:
    print(True)
else:
    print(False)


dic = {'one':[1],"two":[1,2],"Three":[1,2,3],"Four":[1,2,3,4]}
dic['Three'].append(3)
print(dic)

dic["Five"] =[1,2,3,4,5]
print(dic)

