

string = "slknlksdnlkksnvlkvlkvddlkvnzknv;lknv;kdzvnd;lkn;kjvvvkkm"
print(len(string))

strrr = "New" + "found" + "land"
print(strrr)

# join method
str1=("&").join(["hab","tab","lab","cab"])
print(str1)

str2 = str1.split("&")
print(str2)
for x in str2:
    print(x)

bis = "-".join(['skhf','skfskb','skjdfjs','sbksjb'])
print(bis)


# Partition method

part = "unforgetable"
sub = part.partition("forget")
print(sub)
for t in sub:
    print(t)
# undrscore(_) is used when you don't want to use or unused item
pen,_,pert = "first-second".partition("-")
print(pen)
print(pert)

# format method

strin = " this is {}, that is the {}".format("nothing","something")
print(strin)

str12 = ("i am {0} and i am a {1} beacause i am {0}").format("aravind","goodboy")
print(str12)

str123 = "this is a {longitude}, and there is a {latitude}".format(longitude = "60N", latitude = "25S")
print(str123)

tup = (3.45,34.54,3.546,3.485)

print("i have values x ={tup[0]}, y = {tup[1]}, z ={tup[2]}, w =(tup[3])".format(tup=tup))


import math

mat = " Math constants {m.pi},{m.e}".format(m=math)
print(mat)

mat = " Math constants {m.pi:.3f},{m.e:.2f}".format(m=math)
print(mat)

