# class Employee:

#     def showEmployeeData(self):
#         print('John', '39', '$20,000')

# obj = Employee()
# obj.showEmployeeData()

class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender
        self.email = self.generateEmail
        
    def generateEmail(self):
        return f'{self.name}@company.com'
    
    def showInfo(self):
        print(self.name, self.age, self.salary, self.gender, self.email)

    @classmethod
    def changeCompanyName(cls, newName):
        cls.company = newName

    @classmethod
    def info():
        print('This is a class for creating employee objects and it requires...')

    class Job:
        
        def __init__(self, designation, department, responsibility):
            self.designation = designation
            self.designation = designation
            self.designation = designation

obj = Employee('John', '39', '$20,000', 'male')
obj.showInfo()
print(obj)



##Sub classes:
