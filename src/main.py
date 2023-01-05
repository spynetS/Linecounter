
# list all files and their lines
# group files and lines
# total of lines
# ignore files (defaults)
# ignore folders (defaults)
# ignore extetions (defaults)
# ignore comments
# ignore empty lines
from flagser import *

# create flags
class Lf(Flag):
    shortFlag = "-lf"
    description="lists all files and their line counts"

    def onCall(self, args):
        print("all files and thier line counets")

class T(Flag):
    shortFlag = "-t"
    description="outputs total of lines countet"

    def onCall(self, args):
        print("total")
# checks flags
a = FlagManager([Lf(), T()])
a.check()



