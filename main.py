# # OBJECT IS A GROUP OF INFORMATION THAT BELONG TOGETHER

# from unicodedata import name


# names = ["Vera", "chuck", "Samantha", "Roberto", "Joe", "Dave", "Tina"]
# salaries = [2000,1800,1800,2100,2000,2200,2300]

# count = len(names)

# for c in range(count):
#     print(f'{names[c]}, ${salaries[c]}')


##Class name begin with capital letter
class Employee:
    def __init__(self,name,salary): #dunder methods __method__, dunder init is called when the object is created
#self is a reference to the object itself,the way of the class to reference a especific object
#is through the parameter "self"
        self.name = name
        self.salary = salary
class Mechanic(Employee):
    job_title = "Mechanic2"
    
class Attendant(Employee):
    job_title = "Station Attendant"
    
class Cook(Employee):
    job_title = "Cook"

class Manager(Employee):
    job_title = "Manager"



listOfEmployee = [Manager("vera",2000),Attendant("chuck",1800),
                  Attendant("Samantha",1800),Cook("Roberto",2100),
                  Mechanic("Joe",2000),Mechanic("Dave",2200),
                  Mechanic("Tina",2300)]
                  
for e in listOfEmployee:
    print(f'{e.name}s salary is ${e.salary}, {e.job_title}')
