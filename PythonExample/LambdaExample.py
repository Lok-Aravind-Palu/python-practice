def double(x):
    return x * 2


doub = lambda x: x * 2

if doub(5) == double(5):
    print("Yes they both are the same")
else:
    print("Nope they are not")
    
#Lambda testing for multiple parameters
test = lambda x, y, z: x * y * z

print(test(5, 6, 7))
