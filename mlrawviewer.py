import sys 

from sys import argv,stdout,stderr,exit
from os.path import abspath,split,exists,isdir
from os import listdir
from Config import config
from Viewer import Viewer,PerformanceLog

programpath = abspath(split(argv[0])[0])
if getattr(sys,'frozen',False):
    programpath = sys._MEIPASS
    # Assume we have no console, so try to redirect output to a log file...somewhere
    #try:
    sys.stdout = file(config.logFilePath(),"a") 
    sys.stderr = sys.stdout
    #except:
    #    pass

print("MlRawViewer v"+config.versionString()+"\n(c) Andrew Baldwin & contributors 2013-2014")

def main():
    rmc = Viewer()
    arg = None
    isfile = True
    if len(argv)>1:
        arg = abspath(argv[1])
        if not exists(arg):
            arg = None
        elif isdir(arg):
            isfile = False
            dngs = [f for f in listdir(arg) if f.lower().endswith(".dng")]
            if len(dngs)>0:
                isfile = True
    if arg and isfile:
        rmc.load(abspath(arg))
    else:
        rmc.openBrowser(arg)
    
    ret = rmc.run()
    PerformanceLog.PLOG_PRINT()
    
    return ret

if __name__ == '__main__':
    exit(main())
