import os
import pathlib

class File:
    def __init__(self, path = "", lines=0):
        self.path = path
        self.lines = lines
    def __lt__(self, idk):
        return self.lines > idk

class Reader:

    def __init__(self):
        self.longestPath = 0;
        self.longestEx = 0;
        self.paths = ["./"]
        self.ignoredFiles = ["build.sh"]
        self.ignoredFolders = ["./node_modules","./venv"]
        self.extentions = ["py", "sh", "java", "c", "cpp", "h", "html", "js","css","ts","bash", "cs", "c3"]
        self.ignoredExtentions = []
        self.ignoreNames = ["node_modules"]

    def setIgnoreNames(self,names):
        print(names)
        self.ignoreNames=names

    def count(self, filename):
        l = 0
        with open(filename,("rb")) as f:
            l += (len(f.readlines()))
        return l

    def ignorePath(self,path):
        for name in self.ignoreNames:
            if name in path: return True
        return False

    def readFolders(self):
        files = []
        for path in self.paths:
            if os.path.isfile(path):
                file = File(path,self.count(path))
                files.append(file)
            elif self.ignorePath(path):
                continue
            else:
                if(path[len(path)-1] != "/"): path = path+"/"
                files = files + self.readFolder(path)
        return files

    def readFolder(self,path):
        files = []
        try:
            for filename in os.listdir(path):
                extention = pathlib.Path(path+filename).suffix[1:]

                ignore_extention = extention in self.ignoredExtentions
                extention_exists = (extention in self.extentions or "*" in self.extentions)
                ignore_file = path+filename not in self.ignoredFiles

                # check if we should read this file
                if os.path.isfile(path+filename) and not ignore_extention and extention_exists and ignore_file:

                    if len(path+filename) > self.longestPath: self.longestPath = len(path+filename)
                    if len(extention) > self.longestEx: self.longestEx = len(extention)

                    # read lines
                    files.append(File(path+filename,self.count(path+filename)))

                if not os.path.isfile(path+filename) and path+filename+"/" not in self.ignoredFolders :
                    if not self.ignorePath(path):
                        files = files + self.readFolder(path+filename+"/")
            return files
        except FileNotFoundError as e:
            print("skiping",e)
            return []


    def printFile(self, file):
        print(file.path,((self.longestPath-len(file.path))*" "),file.lines )

