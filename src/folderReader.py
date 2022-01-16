import os
import pathlib
from FileClass import FileClass


class FolderReader:
    valid_sufix = []
    ignore_sufix = []
    ignore_folders = []
    def __init__(self,valid_sufix=[],ignore_sufix=[],ignore_folders=[]):
        self.valid_sufix = valid_sufix;
        self.ignore_sufix = ignore_sufix;
        self.ignore_folders = ignore_folders;

    
    def readFolder(self,path):
        files = []
        currentFile=FileClass()
        for filename in os.listdir(path):
            sufix = pathlib.Path(filename).suffix
            if(sufix!=""):
                if(sufix in self.valid_sufix and len(self.valid_sufix)!=0):
                    currentFile = FileClass(path+filename)
                    file = open(path+filename,("rb"))
                    for line in file:
                        currentFile.increase()
                    files.append(currentFile)
                elif(sufix not in self.ignore_sufix and len(self.ignore_sufix)!=0):
                    currentFile = FileClass(path+filename)
                    file = open(path+filename,("rb"))
                    for line in file:
                        currentFile.increase()
                    files.append(currentFile)
                elif((len(self.ignore_sufix)==0)and (len(self.valid_sufix)==0)):
                    currentFile = FileClass(path+filename)
                    file = open(path+filename,("rb"))
                    for line in file:
                        currentFile.increase()
                    files.append(currentFile)
            
            elif(sufix ==""):
                try:
                    if(path+filename+"/" not in self.ignore_folders):
                        files += (self.readFolder(path+filename+"/"))
                except:
                    pass

        return files;

