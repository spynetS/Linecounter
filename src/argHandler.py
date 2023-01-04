import os
import pathlib
from FileClass import FileClass
from folderReader import FolderReader

class ArgHandler:

    project_path = ["./"]
    common_extensions = [".py", ".c", ".java", ".cpp", ".sh",".js",".jsx",".css", ".html"]
    line_counter = 0
    args = []
    default_ignores = ["./.git","./src/__pycache__"]

    def __init__(self,args):
        self.folderReader = FolderReader([],[],self.default_ignores)
        self.args= args
        self.folderReader.valid_sufix = self.readArgs("-ex")
        #no extention set
        if( len(self.folderReader.valid_sufix) == 0 ):
            self.folderReader.valid_sufix = self.common_extensions

        self.setPath(self.readArgs("-p"))
        self.folderReader.ignore_sufix = self.readArgs("-iex")
        self.folderReader.ignore_folders=self.folderReader.ignore_folders+(self.readArgs("-ida"))
        self.folderReader.valid_sufix = self.folderReader.valid_sufix+(self.readArgs("-exa"))

        lf = True
        for arg in args:
            if(arg=="-h" or arg=="--help"):
                self.printHelp()
                lf = False
            if (arg=="-l"):
                self.printTotalLines()
                lf = False
            if (arg=="-c"):
                self.categorize()
                lf = False
            if (arg=="-a"):
                self.folderReader.valid_sufix = []
            if(arg=='-id'):
                self.folderReader.ignore_folders = self.readArgs("-id")
            if(arg=='-lf'):
                self.printFilesWithLines()

        if(lf):
            self.printFilesWithLines()


    def readArgs(self,tag):
        sufixreader = False
        sufixes = []

        for arg in self.args:
            if(arg[0] == "-"):
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
        print("-l (lines) prints the total amount of lines")
        print("-p (paths) followed by paths is where we look")
        print("-ex (extension) followed file extensions (.py .txt) will override the default ones",self.common_extensions)
        print("-exa (extension) followed file extensions (.py .txt) will add that extetion to counters, the default ones",self.common_extensions)
        print("-a will override all default extentions ",self.common_extensions, "and will count all types of files")
        print("-id (ignore folders) followed by foldersoruces will ignore the folders (./folder/) default is", self.default_ignores)
        print("-ida (ignore folders) followed by foldersoruces will add that folder to the ignored ones  ")
        print("-iex (ignore extension) followed by suffixes will ignore the files with that suffixes")
        print("-c (categorize) will count the files and output the total amount of lines in every extention")
        print()
        print("example 1: -l -ex .py")
        print("         will print total lines of all .py files")
        print()
        print("example 2: -lf -ex .py")
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

    def categorize(self):
        types = {}
        for path in self.project_path:
            for file in self.folderReader.readFolder(path):
                su = pathlib.Path(file.filename).suffix
                if su in types:
                    types[su] = types[su] + file.linecount
                else:
                    types[su] = file.linecount

        types = {k: v for k, v in sorted(types.items(), key=lambda item: item[1])}
        for su in types:
            tab = 10-len(su)
            print(su,(tab*" "),types[su]," lines")


    def printFilesWithLines(self):
        files = {}
        for path in self.project_path:

            for file in self.folderReader.readFolder(path):


                files[file.filename] = file.linecount

                self.line_counter += file.linecount

        files = {k: v for k, v in sorted(files.items(), key=lambda item: item[1])}
        for file in files:
            tab = self.folderReader.largestPath+10-len(file) if self.folderReader.largestPath-len(file) + 5>0 else 1;
            print(file+(tab*" ")+str(files[file])+" lines")

    def setPath(self,path):
        if len(path) > 0:
            if(path[0][len(path)-1] != "/"):
                self.project_path = [(path[0]+"/")]
            else:
                self.project_path = path

