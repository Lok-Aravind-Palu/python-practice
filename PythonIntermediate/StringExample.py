def check_path_string():
    path = r"c:User\aravind\table\newfolder"
    print(path)


#
def immutable_check():
    c = "oreo"
    c.capitalize()
    print(c)
    print(c.capitalize())


print("this is the \" string")
print('this is the \' string out')
print("this is the \\ string")
print("\345")
print("\xe5")
print("123".isdigit())
print("this is {0}, and i am a {1}".format("aravind","software engineer"))
print("ab afsd".split())


check_path_string()

immutable_check()