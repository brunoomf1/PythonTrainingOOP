from os.path import exists
import os

def saveFile(file):
    file.close()

class Folders:
    
    def check_folder_exist(path):
        check = exists(path)
        return check
    
    def create_folder(path):
        if Folders.check_folder_exist(path) == False:
            os.mkdir(path)
            

class CreateFile:
    def __init__(self, _name = 'file', _format = 'txt',_path = "files"):
        self.name_format= f'{_path}/{_name}.{_format}'
        self.name = _name
        self.format = _format
        self.path = _path
  
        Folders.create_folder(self.path)
        
        if exists(self.name_format) == False:
           file = open(self.name_format,'x')
           saveFile(file)
        
        elif exists(self.name_format) == True:
            res = input('arquivo ja esxiste, deseja substituir? (y/n)')
            if res == "y":
                file = open(self.name_format,'w')
                saveFile(file)



class OpeningFile():
    def __init__(self, _name = 'file', _format = 'txt',_path = "files"):
        name_format= f'{_path}/{_name}.{_format}'
        self.name = _name
        self.format = _format
        self.path = _path 

    def open_file(name_format):
        if exists(self.name_format) == False:
           CreateFile(self.name,self.format,self.path)
        
        return open(self.name_format,'r+')
