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

# create flags
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

Lf = Flag(shortFlag="-lf",description="lists all files and their line counts", onCall = lambda args: lf())

T = Flag(shortFlag="-t",description="outputs total of lines counted", onCall = lambda args:print("total:",total))

G = Flag(shortFlag="-g",description="outputs total of lines grouped by extention", onCall = lambda args: g())

All = Flag(shortFlag="-a",description="sets extentions to all", onCall = lambda args: reader.extentions.append("*"))

Id = Flag(shortFlag="-id",description="sets folders to the ignored ones", onCall = lambda args: setPath(reader.ignoredFolders,args))

Ex = Flag("-ex",description="sets the extentions to be counted", onCall = lambda args:setList(reader.extentions, args))

Iex = Flag("-iex",description="sets the extentions to not be counted", onCall = lambda args: setList(reader.ignoredExtentions,args))

Paths = Flag("-p",description="sets starting paths", onCall = lambda args:setPath(reader.paths, args))

# checks flags
options = FlagManager([Id,Ex,Iex,Paths,All])
options.description = "Linecounter (lctr) is a simple linecounter program to count source code lines"

if options.check() <= 0 and len(sys.argv) > 1 :
    p = sys.argv[len(sys.argv)-1]
    if(p[0] != "-") :
        reader.paths.clear()
        reader.paths.append(p)

for file in reader.readFolders():
    files.append(file)

    ex = pathlib.Path(file.path).suffix
    if(ex in extentions):
        extentions[ex] = extentions[ex] + file.lines
    else:
        extentions[ex] = file.lines

    total += file.lines

files.sort()

commands = FlagManager([Lf, T, G])
if commands.check() <= 0 :
    lf()
    print("total:",total)

