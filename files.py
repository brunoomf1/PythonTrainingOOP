from os.path import exists

def saveFile(file):
    file.close()


def createFile(name = 'file',format = 'txt'):
    nameFormat = f'{name}.{format}'


    if exists(nameFormat) == False:
        file = open(nameFormat,'x')
        save_file(file)

    elif exists(nameFormat) == True:
        res = input('arquivo ja esxiste, deseja substituir? (y/n)')
        if res == "y":
            file = open(nameFormat,'w')
            save_file(file)


def openFile(name,format):
    nameFormat = f'{name}.{format}'
    file = open(nameFormat,'r+')
    return file

puts('teste')
