#!/usr/bin/python
from flagser import *
from fileReader import Reader
import pathlib
import sys
from printer import print_table

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

def l():
    for file in files: reader.printFile(file)

def lf():
    #for file in files: reader.printFile(file)
    filees = []
    SUM = ["SUM",0,0,0,0,0]
    for fil in files:
        filees.append([fil.path,fil.lines,fil.comments,fil.empty,fil.empty+fil.lines+fil.comments])
        SUM[1] += fil.lines
        SUM[2] += fil.comments
        SUM[3] += fil.empty
        SUM[4] += fil.lines+fil.comments+fil.empty
    print_table(["FILE","LINES","COMMENTS","EMPTY","SUM"],filees,SUM,sort=1)

def g():
    for file in files:
        ex = pathlib.Path(file.path).suffix
        if(ex in extentions):
            extentions[ex] = extentions[ex] + file.lines+file.empty+file.comments
        else:
            extentions[ex] = file.lines+file.empty+file.comments

    for file in extentions:
        print(file,(reader.longestEx-len(file))*" ",extentions[file])

def gf():
    filees = []
    SUM = ["SUM",0,0,0,0,0]
    for fil in files:
        ex = pathlib.Path(fil.path).suffix
        add = False
        for fil1 in filees:
            if fil1[0] == ex:
                fil1[1] += 1
                fil1[2] += fil.lines
                fil1[3] += fil.comments
                fil1[4] += fil.empty
                fil1[5] += fil.lines+fil.comments+fil.empty
                add = True
        if not add:
            filees.append([ex,1,fil.lines,fil.comments,fil.empty,fil.lines+fil.comments+fil.empty])

        SUM[1] += 1
        SUM[2] += fil.lines
        SUM[3] += fil.comments
        SUM[4] += fil.empty
        SUM[5] += fil.lines+fil.comments+fil.empty


    print_table(["LANGUAGE","FILES","LINES","COMMENTS","EMPTY","SUM"],filees,SUM,sort=2)

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
options.description = "Linecounter (lctr) is a simple linecounter program to count source code lines\n Usage: lctr [options] [path]"

## sets the path to the last argument of it is not a flag
if options.check() <= 0 and len(sys.argv) > 1 :
    p = sys.argv[len(sys.argv)-1]
    if(p[0] != "-") :
        reader.paths.clear()
        reader.paths.append(p)

## its here we do the counting
if "-h" not in sys.argv and "--help" not in sys.argv:
    for file in reader.readFolders():
        if file.path not in ignoreFiles:
            files.append(file)

            total += file.lines+file.comments+file.empty

    files.sort()


commands = FlagManager([
    Flag(shortFlag="-l",description="lists all files and their line counts ", onCall = lambda args: l()),
    Flag(shortFlag="-lf",description="lists all files and their line counts format", onCall = lambda args: lf()),
    Flag(shortFlag="-t",description="outputs total of lines counted", onCall = lambda args:print("total:",total)),
    Flag(shortFlag="-g", description="outputs total of lines grouped by extention format", onCall = lambda args: g()),
    Flag(shortFlag="-gf",description="outputs total of lines grouped by extention format format", onCall = lambda args: gf()),
])

if commands.check() <= 0 :
    gf()
