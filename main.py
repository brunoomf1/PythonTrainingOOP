import employee
import report
from report import AccoutingReport
from report import StaffingReport
from report import ScheduleReport
from shift import MorningShift
from shift import AfternoonShift
from files import OpeningFile

# OBJECT IS A GROUP OF INFORMATION THAT BELONG TOGETHER

##Class name begin with capital letter

file = OpeningFile.open_file()

listOfEmployee = [employee.Manager("Vera Schmidt",2000,MorningShift()),
                  employee.Attendant("Chuck Norris",1800,MorningShift()),
                  employee.Attendant("Samantha Carrington",1800,AfternoonShift()),
                  employee.Cook("Roberto Jacketti",2100,MorningShift()),
                  employee.Mechanic("Ringo Rama",1900,MorningShift()),
                  employee.Mechanic("Dave Dreibig",2200,MorningShift()),
                  employee.Mechanic("Tina River",2300,AfternoonShift()), 
                  employee.Mechanic("Chuck Rainey",2300,AfternoonShift())
]
                  

report = [
    AccoutingReport(listOfEmployee),
    StaffingReport(listOfEmployee),
    ScheduleReport(listOfEmployee)
]

for r in report:
    r.print_report()
    file.write(r.print_report())