#!/usr/bin/python
from flagser import *
from fileReader import Reader
import pathlib
import sys

# The thought is the flags should change the readers booleans
# this is so the commands runs in the correct order (you dont want to
# print all lines before the path is set 'lctr -lf ./path' )

reader = Reader()

total = 0
extentions = {}
files = []
ignoreFiles=[]
ignoreNames = []


# create flags
def setIgnoreFiles(args):
    global ignoreFiles
    ignoreFiles=args

def lf():
    for file in files: reader.printFile(file)
def g():
    for file in extentions:
        print(file,(reader.longestEx-len(file))*" ",extentions[file])

def setList(addto,addfrom):
    addto.clear()
    for arg in addfrom:
        # if(arg[len(arg)-1] == "/"): arg = arg[:-1]
        addto.append(arg)

def setPath(addto,addfrom):
    addto.clear()
    for arg in addfrom:
        if(arg[len(arg)-1] != "/"): arg = arg+"/"
        addto.append(arg)


# checks flags
options = FlagManager([
    Flag(shortFlag="-a",description="sets extentions to all", onCall = lambda args: reader.extentions.append("*")),
    Flag(shortFlag="-id",description="sets folders to the ignored ones", onCall = lambda args: setPath(reader.ignoredFolders,args)),
    Flag(shortFlag="-in",description="sets names to the ignore", onCall = reader.setIgnoreNames),
    Flag(shortFlag="-if",description="sets files to the ignored ones", onCall = setIgnoreFiles),
    Flag("-ex",description="sets the extentions to be counted", onCall = lambda args:setList(reader.extentions, args)),
    Flag("-iex",description="sets the extentions to not be counted", onCall = lambda args: setList(reader.ignoredExtentions,args)),
    Flag("-p",description="sets starting paths", onCall = lambda args:setPath(reader.paths, args)),
])
options.description = "Linecounter (lctr) is a simple linecounter program to count source code lines"

## sets the path to the last argument of it is not a flag
if options.check() <= 0 and len(sys.argv) > 1 :
    p = sys.argv[len(sys.argv)-1]
    if(p[0] != "-") :
        reader.paths.clear()
        reader.paths.append(p)

if "-h" not in sys.argv and "--help" not in sys.argv:
    for file in reader.readFolders():
        if file.path not in ignoreFiles:
            files.append(file)

            ex = pathlib.Path(file.path).suffix
            if(ex in extentions):
                extentions[ex] = extentions[ex] + file.lines
            else:
                extentions[ex] = file.lines

            total += file.lines

    files.sort()

commands = FlagManager([
    Flag(shortFlag="-lf",description="lists all files and their line counts", onCall = lambda args: lf()),
    Flag(shortFlag="-t",description="outputs total of lines counted", onCall = lambda args:print("total:",total)),
    Flag(shortFlag="-g",description="outputs total of lines grouped by extention", onCall = lambda args: g()),
])

if commands.check() <= 0 :
    lf()
    print("total:",total)

