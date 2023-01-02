import os
import pathlib
from FileClass import FileClass
from folderReader import FolderReader

class ArgHandler():

    project_path = ["./"]
    line_counter = 0
    args = []
    folderReader = FolderReader([],[],["./.git","./src/__pycache__"])

    def __init__(self,args):
        self.args= args
        self.folderReader.valid_sufix=self.readArgs("-su")
        self.setPath(self.readArgs("-p"))
        self.folderReader.ignore_folders= self.readArgs("-id")
        self.folderReader.ignore_sufix= self.readArgs("-isu")

        lf = True
        for arg in args:
            if(arg=="-h" or arg=="--help"):
                self.printHelp()
            if (arg=="-l"):
                self.printTotalLines()
                lf = False
        if(lf):
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
        paths = []
        for arg in self.args:
            if(arg =="-p"):
                paths.append(self.args[i])
            i+=1
        self.setPath(paths)


    def printHelp(self):
        print()
        print("-l prints the total amount of lines")
        print("-p followed by paths is where we look")
        print("-su followed file extensions (.py .txt) if you want to specify which files to list+")
        print("-id followed by foldersoruces will ignore the folders (./folder/) ")
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
        for path in self.project_path:
            for file in self.folderReader.readFolder(path):
                self.line_counter += file.linecount
        print("total: "+str(self.line_counter))

    def printFilesWithLines(self):
        for path in self.project_path:

            for file in self.folderReader.readFolder(path):

                tab = 60-len(file.filename) if 60-len(file.filename)>0 else 1;

                print(file.filename+(tab*" ")+str(file.linecount)+" lines")

                self.line_counter += file.linecount

        print("total: "+str(self.line_counter))

    def setPath(self,path):
        if len(path) > 0:
            self.project_path = path
