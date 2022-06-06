# OBJECT IS A GROUP OF INFORMATION THAT BELONG TOGETHER

from unicodedata import name


names = ["Vera", "chuck", "Samantha", "Roberto", "Joe", "Dave", "Tina"]
salaries = [2000,1800,1800,2100,2000,2200,2300]

count = len(names)

for c in range(count):
    print(f'{names[c]}, ${salaries[c]}')
    
    class Employee:
        def __init__(self,name,salary):
            self.name = name
            self.salay = salary