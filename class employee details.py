class Employee:
    def __init__(self,name,age,salary,gender,compony):
        self.name = name
        self.age = age
        self.gender = gender
        self.compony = compony
        self.salary = salary

    def employee_details(self):
        print("Name of employee: ", self.name)
        print("Age of employee: ", self.age) 
        print("gender of employee: ", self.gender)
        print("Compony of employee: ", self.compony)
        print("Salary of employee: ", self.salary)

Emp = Employee("Ajinkya", 29, 1000000, "male", "Google")
Emp.employee_details()
           

