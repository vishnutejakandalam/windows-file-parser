import os
import sys
path = ""
drives = [ chr(x) + ":" for x in range(65,90) if os.path.exists(chr(x) + ":") ]
def printlist(li):
    dicto=  {}
    global path
    n = len(li)
    for i in range(0,n):
        print(i+1,li[i],sep="->")
        dicto[i+1] = li[i]
    try:
        val = int(input("enter the number of the directory to get into"))
    except:
        print("INVALID INPUT DUDE...!   ")
        sys.exit(0)
    if dicto[val].__contains__("."):
        print("OPENING YOUR FILE ....")
        os.startfile(path+dicto[val])
        sys.exit(0)
    else:
        path +=dicto[val]+"/"
    print(path)
    return path


path = printlist(drives)
while True:
    dictos = os.listdir(path)
    path = printlist(dictos)
    