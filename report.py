

def report_salary(listOfEmployee):
    print('          Accounting           ')
    print('============================ ') 
    for e in listOfEmployee:
        print(f'{e.name}s salary is ${e.salary}')
        #print('--------------------------------')
        
    print('=============================') 
    print('                             ')

     
def report_titles(listOfEmployee):
    print('          Staffing           ')
    print('============================ ') 
    
    for e in listOfEmployee:
        print(f'{e.name}s is a {e.job_title}')
        #print('--------------------------------')

    
    print('=============================') 
    print('                             ')