from os.path import exists 

def save_file(file):
    file.close()


def createFile(name = 'file',format = 'txt'):
    nameFormat = f'{name}.{format}'
    if exists(nameFormat) == False:
        file = open(nameFormat,'x')
        
    if exists(nameFormat) == True:
        res = input('arquivo ja esxiste, deseja substituir? (y/n)')
        if res == "y":
            file = open(nameFormat,'w')
      
    save_file(file)
    

def open_file(name):
    if exists(name) == False:
        print (exists(name))
        createFile(name)
    file = open(name,'+')
    return(file)

