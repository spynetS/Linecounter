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

    def countLines(self,files,path,filename):
        currentFile=FileClass()
        currentFile = FileClass(path+filename)
        file = open(path+filename,("rb"))
        with open(path+filename,("rb")) as f:
            currentFile.increase(len(f.readlines()))

        files.append(currentFile)

        return files;

    def readFolder(self,path):
        files = []
        currentFile=FileClass()
        for filename in os.listdir(path):
            # sufix is the fileextension
            sufix = pathlib.Path(filename).suffix

            if(sufix!=""):

                if sufix in self.valid_sufix and sufix not in self.ignore_sufix:
                    files = self.countLines(files,path,filename)

            elif(sufix ==""):
                try:
                    if(path+filename+"/" not in self.ignore_folders):
                        files += (self.readFolder(path+filename+"/"))
                except:
                    pass

        return files;

