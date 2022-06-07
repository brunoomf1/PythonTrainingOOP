class Employee:
    def __init__(self,name,salary): #dunder methods __method__, dunder init is called when the object is created
#self is a reference to the object itself,the way of the class to reference a especific object
#is through the parameter "self"
        self.name = name
        self.salary = salary
        
class Mechanic(Employee):
    job_title = "Mechanic"
    
class Attendant(Employee):
    job_title = "Station Attendant"
    
class Cook(Employee):
    job_title = "Cook"

class Manager(Employee):
    job_title = "Manager"


