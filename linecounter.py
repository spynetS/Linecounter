import os
import pathlib
import sys

'''
total lines -a or nothing
help -h
lines in every file -af
only file type -su
'''

class FileClass:
    linecount = 0
    filename = ""
    def __init__(self,filename="no file name",linecount=0):
        self.linecount=linecount
        self.filename=filename

    def increase(self):
        self.linecount+=1;
    def __str__(self):
        return ("filename: "+self.filename+" linecount: "+str(self.linecount))


project_path = ""
line_counter = 0
valid_sufix = []

def readFolder(path):
    files = []
    global valid_sufix
    currentFile=FileClass()
    for filename in os.listdir(path):
        sufix = pathlib.Path(filename).suffix
        if(sufix !="" and (sufix in valid_sufix or len(valid_sufix)==0)): #if it is a file
            currentFile = FileClass(path+filename)
            file = open(path+filename,("rb"))
            for line in file:
                currentFile.increase()
            files.append(currentFile)
        
        elif(sufix ==""):
            try:
                files += (readFolder(path+filename+"/"))
            except:
                pass

    return files;

def getValidSufixes():
    sufixreader = False
    sufixes = []

    for arg in sys.argv:
        if(sufixreader==True):
            sufixes.append(arg)
        if("-" in arg):
            sufixereader = False
            if(arg == "-su"):
                sufixreader = True
    return sufixes

def printHelp():
    print()
    print("-l prints the total amount of lines")
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

def printTotalLines():
    global line_counter
    for file in readFolder("./"):
        line_counter += file.linecount
    print("total: "+str(line_counter))

def printFilesWithLines():
    global line_counter
    for file in readFolder("./"):
        print(file)
        line_counter += file.linecount
    print("total: "+str(line_counter))
    
def argHandler():
    global valid_sufix
    valid_sufix=getValidSufixes()
    if(len(sys.argv)==1):
        printHelp()
        
    for arg in sys.argv:
        if(arg=="-h"):
            printHelp()
        if (arg=="-l"):
            printTotalLines()
        if(arg=="-lf"):
            printFilesWithLines()

if(__name__=="__main__"):
    argHandler()

