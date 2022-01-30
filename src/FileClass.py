class FileClass:
    linecount = 0
    filename = ""
    def __init__(self,filename="no file name",linecount=0):
        self.linecount=linecount
        self.filename=filename

    def increase(self,amount=1):
        self.linecount+=amount;

    
    def __str__(self):
        return ("filename: "+self.filename+" linecount: "+str(self.linecount))