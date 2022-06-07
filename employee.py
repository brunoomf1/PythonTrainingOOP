class Employee:
    def __init__(self,full_name,salary): #dunder methods __method__, dunder init is called when the object is created
#self is a reference to the object itself,the way of the class to reference a especific object
#is through the parameter "self"

        splited_name = full_name.split(" ")
        self.first_name = splited_name[0]
        self.last_name = splited_name[1]
        self.salary = salary
        
class Mechanic(Employee):
    job_title = "Mechanic"
    
class Attendant(Employee):
    job_title = "Station Attendant"
    
class Cook(Employee):
    job_title = "Cook"

class Manager(Employee):
    job_title = "Manager"


