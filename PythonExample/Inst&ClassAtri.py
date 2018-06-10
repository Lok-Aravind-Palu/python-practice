employ = []
class classAtributes:

    employe_company = "comcast"

    def __init__(self,name,id = 132):
        self.name = name
        self.id = id
        employ.append(self)


    def __str__(self):
        return "Employee : " + self.name

aravind = classAtributes("aravind")
print(classAtributes.employe_company)
print(aravind)

