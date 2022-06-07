import employee as em

def report_salary(listOfEmployee):
    print('          Accounting           ')
    print('============================ ') 
    for e in listOfEmployee:
        print(f'{em.Employee.get_full_name(e)}, ${e.salary}')
        #print('--------------------------------')
        
    print('=============================') 
    print('                             ')

     
def report_titles(listOfEmployee):
    print('          Staffing           ')
    print('============================ ') 
    
    for e in listOfEmployee:
        print(f'{em.Employee.get_full_name(e)}, {e.job_title}')
        #print('--------------------------------')

    
    print('=============================') 
    print('                             ')