import sys
import time

from argHandler import ArgHandler

common_extensions = [".py", ".c", ".java", ".cpp", ".sh"]

if(__name__=="__main__"):
    #start = (time.time())
    argHandler = ArgHandler(sys.argv)
    #end = (time.time())
    #print("Time taken:",end-start)

