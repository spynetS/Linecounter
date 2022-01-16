import os
import pathlib
from FileClass import FileClass
from folderReader import FolderReader

class ArgHandler():
    
    project_path = "./"
    line_counter = 0
    args = []

    def __init__(self,args):
        self.args= args
        FolderReader.valid_sufix=self.getValidSufixes()
        self.get_path()
        if(len(args)==1):
            self.printHelp()
        for arg in args:
            if(arg=="-h"):
                self.printHelp()
            if (arg=="-l"):
                self.printTotalLines()
            if(arg=="-lf"):
                self.printFilesWithLines()
    
    def get_path(self):
        i = 1
        for arg in self.args:
            if(arg =="-p"):
                self.setPath(self.args[i])
            i+=1
    
    def getValidSufixes(self):
        sufixreader = False
        sufixes = []

        for arg in self.args:
            if(sufixreader==True):
                sufixes.append(arg)
            if("-" in arg):
                sufixereader = False
                if(arg == "-su"):
                    sufixreader = True
        return sufixes

    def printHelp(self):
        print()
        print("-l prints the total amount of lines")
        print("-p sets the origin path")
        print("-su followed file extensions (.py .txt) if you want to specify which files to list+")
        print("-lf prints all files with it's lines counts")
        print()
        print("example 1: -l -su .py")
        print("         will print total lines of all .py files")
        print()
        print("example 2: -lf -su .py")
        print("         will print files with total lines of all .py files")
        print()
        print("example 3: -l")
        print("         will print total lines of all files")
        print()
        print("example 4: -lf")
        print("         will print files with total lines of all files")

    def printTotalLines(self):
        for file in FolderReader.readFolder(self.project_path):
            self.line_counter += file.linecount
        print("total: "+str(self.line_counter))

    def printFilesWithLines(self):
        for file in FolderReader.readFolder(self.project_path):
            print(file)
            self.line_counter += file.linecount
        print("total: "+str(self.line_counter))

    def setPath(self,path):
        self.project_path = path
