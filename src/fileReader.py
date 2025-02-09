import os
import pathlib
#idk
##idk
##askd
##asd
##asjd


class File:
    def __init__(self, path = "", lines=0):
        self.path = path
        self.lines = lines
        self.comments = 0
        self.empty = 0
        self.count()

    def __lt__(self, idk):
        return self.lines > idk

    def is_comment(self, line):
        comments = ['#',"//","--"]
        comment_blocks = ["/*","*/","'''","'''"] #start, followed by end

        for comment in comments:
            if line[0:len(comment)] == comment:
                return True
        # TODO
        # Comment blocks
        return False

    def count(self):

        with open(self.path,("r")) as f:
            try:
                lines = f.readlines()
            except:
                # this is not correct but better then 0 i guess
                lines = f.read().split("\n")

            for i in lines:
                if i == "\n":
                    self.empty += 1
                elif not self.is_comment(i):
                    self.lines+=1
                else:
                    self.comments+=1


class Reader:

    def __init__(self):
        self.longestPath = 0;
        self.longestEx = 0;
        self.paths = ["./"]
        self.ignoredFiles = ["build.sh"]
        self.ignoredFolders = ["node_modules",".venv"]
        self.extentions = ["py", "sh", "java", "c", "cpp", "h", "html", "js","css","ts","bash", "cs", "c3","md","org","bat"]
        self.ignoredExtentions = []
        self.ignoreNames = ["node_modules"]

    def setIgnoreNames(self,names):
        print(names)
        self.ignoreNames=names


    def ignorePath(self,path):
        for name in self.ignoreNames:
            if name in path: return True
        return False

    def readFolders(self):
        '''
        returns files in folder
        '''
        files = []
        for path in self.paths:
            if os.path.isfile(path):
                file = File(path)
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
                    files.append(File(path+filename))

                if not os.path.isfile(path+filename) and path+filename+"/" not in self.ignoredFolders :
                    if not self.ignorePath(path):
                        files = files + self.readFolder(path+filename+"/")
            return files
        except FileNotFoundError as e:
            print("skiping",e)
            return []


    def printFile(self, file):
        print(file.path,((self.longestPath-len(file.path))*" "),file.lines+file.empty+file.comments)
