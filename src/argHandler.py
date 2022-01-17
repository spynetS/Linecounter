import os
import pathlib
from FileClass import FileClass
from folderReader import FolderReader

class ArgHandler():
    
    project_path = "./"
    line_counter = 0
    args = []
    folderReader = FolderReader([],[],["./.git","./src/__pycache__"])

    def __init__(self,args):
        self.args= args
        self.folderReader.valid_sufix=self.readArgs("-su")
        self.get_path()
        self.folderReader.ignore_folders= self.readArgs("-if")
        self.folderReader.ignore_sufix= self.readArgs("-isu")
        if(len(args)==1):
            self.printHelp()
        for arg in args:
            if(arg=="-h"):
                self.printHelp()
            if (arg=="-l"):
                self.printTotalLines()
            if(arg=="-lf"):
                self.printFilesWithLines()


    def readArgs(self,tag):
        sufixreader = False
        sufixes = []

        for arg in self.args:
            if("-" in arg):
                sufixreader = False
                if(arg == tag):
                    sufixreader = True
                    continue
            if(sufixreader==True):
                sufixes.append(arg)

        return sufixes

    def get_path(self):
        i = 1
        for arg in self.args:
            if(arg =="-p"):
                self.setPath(self.args[i])
            i+=1
    

    def printHelp(self):
        print()
        print("-l prints the total amount of lines")
        print("-p sets the origin path")
        print("-lf prints all files with it's lines counts")
        print("-su followed file extensions (.py .txt) if you want to specify which files to list+")
        print("-if followed by foldersoruces will ignore the folders (./folder/) ")
        print("-isu followed by suffixes will ignore the files with that suffixes")
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
        for file in self.folderReader.readFolder(self.project_path):
            self.line_counter += file.linecount
        print("total: "+str(self.line_counter))

    def printFilesWithLines(self):
        for file in self.folderReader.readFolder(self.project_path):
            print(file.filename+((60-len(file.filename) if (60-len(file.filename)>0) else 1 )*" ")+str(file.linecount)+" lines")
            self.line_counter += file.linecount
        print("total: "+str(self.line_counter))

    def setPath(self,path):
        self.project_path = path
