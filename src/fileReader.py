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
        self.extentions = ["py", "sh", "java", "c", "cpp", "hmtl", "js","css","ts","bash"]
        self.ignoredExtentions = []

    def count(self, file):
        with open(file.path,("rb")) as f:
            file.lines += (len(f.readlines()))

    def readFolders(self):
        files = []
        for path in self.paths:
            files = files + self.readFolder(path)
        return files

    def readFolder(self,path):
        files = []
        for filename in os.listdir(path):
            extention = pathlib.Path(path+filename).suffix[1:]

            if os.path.isfile(path+filename) and extention not in self.ignoredExtentions and extention in self.extentions and path+filename not in self.ignoredFiles:

                if len(path+filename) > self.longestPath: self.longestPath = len(path+filename)
                if len(extention) > self.longestEx: self.longestEx = len(extention)

                currentFile = File(path+filename)
                # read lines
                self.count(currentFile)
                files.append(currentFile)

            if not os.path.isfile(path+filename) and path+filename not in self.ignoredFolders :
                files = files + self.readFolder(path+filename+"/")
        return files

    def printFile(self, file):
        print(file.path,((self.longestPath-len(file.path))*" "),file.lines )










