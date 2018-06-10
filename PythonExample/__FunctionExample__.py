students = []


def get_student_names():
    student_names = []
    for student in students:
        student_names = student
    return student_names


def print_student_namse():
    student_names = get_student_names()
    print(student_names)


def add_names(name):
    students.append(name)


add_names("Aravind")
print_student_namse()


#
def print_studentnames(name, id):
    print(name, id)


print_studentnames("aravind", 132)


#
def def_name_student(name, id=132):
    print(name, id)


def_name_student("aravind")


#
def var_arguments(name, *args):
    print(name)
    print(args)


var_arguments("shawn", "matt", 23,None,True,"comcast")

#
def var_keywordarguments(name, **kwargs):
    print(name)
    print(kwargs["floor"],kwargs["Team"])


var_keywordarguments("Ricki",description = "Senior director",Team = "s-pil",floor = "ninth")



guest = ["Rickie","Ravi"]
print(guest[1].title())
