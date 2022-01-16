import os
import pathlib
from FileClass import FileClass


class FolderReader:
    valid_sufix = []
    
    def __init__(self,valid_sufix=[]):
        self.valid_sufix = valid_sufix;
    
    def readFolder(path):
        files = []
        global valid_sufix
        currentFile=FileClass()
        for filename in os.listdir(path):
            sufix = pathlib.Path(filename).suffix
            if(sufix !="" and (sufix in FolderReader.valid_sufix or len(FolderReader.valid_sufix)==0)): #if it is a file
                currentFile = FileClass(path+filename)
                file = open(path+filename,("rb"))
                for line in file:
                    currentFile.increase()
                files.append(currentFile)
            
            elif(sufix ==""):
                try:
                    files += (FolderReader.readFolder(path+filename+"/"))
                except:
                    pass

        return files;

