from os.path import exists

def saveFile(file):
    file.close()


def createFile(name = 'file',formato = 'txt'):
    nameformato = f'{name}.{formato}'


    if exists(nameformato) == False:
        file = open(nameformato,'x')
        saveFile(file)

    elif exists(nameformato) == True:
        res = input('arquivo ja esxiste, deseja substituir? (y/n)')
        if res == "y":
            file = open(nameformato,'w')
            saveFile(file)


def openFile(name,formato):
    nameformato = f'{name}.{formato}'
    if exists(nameformato) == False:
        createFile(name,formato)
    file = open(nameformato,'r+')
    return file


file = open('salary','csv')
