employee = []


class ConsOthExam:

    def __init__(self, name, id=132):
        employee_var = {name: "name", id: "ntid"}
        employee.append(employee_var)

    def __str__(self):
        return "Employee"


aravind = ConsOthExam("aravind")
print(aravind)
