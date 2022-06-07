

def report_salary(listOfEmployee):
    print('          Accounting           ')
    print('============================ ') 
    for e in listOfEmployee:
        print(f'{e.first_name} {e.last_name} s salary is ${e.salary}')
        #print('--------------------------------')
        
    print('=============================') 
    print('                             ')

     
def report_titles(listOfEmployee):
    print('          Staffing           ')
    print('============================ ') 
    
    for e in listOfEmployee:
        print(f'{e.first_name} {e.last_name}s is a {e.job_title}')
        #print('--------------------------------')

    
    print('=============================') 
    print('                             ')