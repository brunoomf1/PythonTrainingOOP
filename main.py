import employee
import report
# OBJECT IS A GROUP OF INFORMATION THAT BELONG TOGETHER

##Class name begin with capital letter

listOfEmployee = [employee.Manager("Vera",2000),employee.Attendant("Chuck",1800),
                  employee.Attendant("Samantha",1800),employee.Cook("Roberto",2100),
                  employee.Mechanic("Joe",2000),employee.Mechanic("Dave",2200),
                  employee.Mechanic("Tina",2300)]
                  
report.report_salary(listOfEmployee)
report.report_titles(listOfEmployee)