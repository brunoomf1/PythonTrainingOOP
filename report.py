
import employee as em
from shift import Shift


class Reporter:
    def __init__(self,emp_list):
        self.emp_list = emp_list
    
class AccoutingReport(Reporter):
   
    def print_report(self):
        print('          Accounting         ')
        print('============================ ') 
        for e in self.emp_list:
            print(f'{em.Employee.get_full_name(e)}   | ${e.salary}')
        #print('--------------------------------')
        
        print('=============================') 
        print('                             ')


class StaffingReport(Reporter):
    
    def print_report(self):
        print('          Staffing           ')
        print('============================ ') 
        
        for e in self.emp_list:
            print(f'{em.Employee.get_full_name(e)}   | {e.job_title}')
            #print('--------------------------------')

        
        print('=============================') 
        print('                             ')

class ScheduleReport(Reporter):
     def print_report(self):
        print('          Schedule            ')
        print('============================== ') 
        
        for e in self.emp_list:
            print(f'    {em.Employee.get_full_name(e)}      ')
            print(f'{e.Shift.get_shift_info()}')

        
        print('===============================') 
        print('                             ')