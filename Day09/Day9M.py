class Employee:
    empCount=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee %d"%Employee.empCount)
    def displayEmployee(self):
        print("Name:",self.name, "Salary:",self.salary)

emp1=Employee("nikhil",9999)
emp1.displayEmployee()
emp1.salary=17000#modify salary attribute
emp1.experience=3#add an experience attribute
emp1.displayEmployee()
emp1.name="Manoj"# modify name atttribute
emp1.displayEmployee()
print(emp1.experience)
#del emp1.salary #delete salary attribute
emp1.displayEmployee()
