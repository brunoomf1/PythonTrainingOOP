import employee
import report
# OBJECT IS A GROUP OF INFORMATION THAT BELONG TOGETHER

##Class name begin with capital letter

listOfEmployee = [employee.Manager("Vera Schmidt",2000),employee.Attendant("Chuck Norris",1800),
                  employee.Attendant("Samantha Carrington",1800),employee.Cook("Roberto Jacketti",2100),
                  employee.Mechanic("Ringo Rama",1900),employee.Mechanic("Dave Dreibig",2200),
                  employee.Mechanic("Tina River",2300), employee.Mechanic("Chuck Rainey",2300)]
                  
report.report_salary(listOfEmployee)
report.report_titles(listOfEmployee)