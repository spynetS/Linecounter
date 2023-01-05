# list all files and their lines
# group files and lines
# total of lines
# ignore files (defaults)
# ignore folders (defaults)
# ignore extetions (defaults)
# ignore comments
# ignore empty lines

from flagser import *
from fileReader import Reader
import pathlib

# The thought is the flags should change the readers booleans
# this is so the commands runs in the correct order (you dont want to
# print all lines before the path is set 'lctr -lf ./path' )

reader = Reader()

lf = False
t = False
g = False

total = 0
extentions = {}
files = []

# create flags
class Lf(Flag):
    shortFlag = "-lf"
    description="lists all files and their line counts"

    def onCall(self, args):
        global files
        for file in files:
            reader.printFile(file)

class T(Flag):
    shortFlag = "-t"
    description="outputs total of lines counted"

    def onCall(self, args):
        global total
        print("total:",total)

class G(Flag):
    shortFlag = "-g"
    description="outputs total of lines grouped by extention"

    def onCall(self, args):
        global extentions
        for file in extentions:
            print(file,(reader.longestEx-len(file))*" ",extentions[file])

class Id(Flag):
    shortFlag = "-id"
    description="sets folders to the ignored ones"

    def onCall(self, args):
        global reader
        reader.ignoredFolders = []
        for arg in args:
            if(arg[len(arg)-1] == "/"): arg = arg[:-1]
            reader.ignoredFolders.append(arg)

class Extentions(Flag):
    shortFlag = "-ex"
    description="sets the extentions to be counted"

    def onCall(self, args):
        global reader
        reader.extentions = []
        for arg in args:
            if(arg[0] == "."): arg = arg[1:]
            reader.extentions.append(arg)

class IgnoredExtentions(Flag):
    shortFlag = "-iex"
    description="sets the extentions to be counted"

    def onCall(self, args):
        global reader
        reader.ignoredExtentions = []
        for arg in args:
            if(arg[0] == "."): arg = arg[1:]
            reader.ignoredExtentions.append(arg)

class Paths(Flag):
    shortFlag = "-p"
    description="sets starting paths"

    def onCall(self, args):
        global reader
        reader.paths = []
        for arg in args:
            if(arg[len(arg)-1] != "/"): arg = arg+"/"
            reader.paths.append(arg)


# checks flags
options = FlagManager([Id(),Extentions(),IgnoredExtentions(),Paths()])
options.check()
print(reader.ignoredExtentions)
for file in reader.readFolders():
    files.append(file)

    ex = pathlib.Path(file.path).suffix
    if(ex in extentions):
        extentions[ex] = extentions[ex] + file.lines
    else:
        extentions[ex] = file.lines

    total += file.lines

files.sort()

commands = FlagManager([Lf(), T(),G()])
commands.check()


