import os
import sys
from colorama import Fore , Style
import asyncio
from tkinter import Tk , filedialog



types_create = (
  "Папка",
  "файл"  
)

types_file = (
    "txt",
    "md",
    "py",
    "bat",
)




def searchplacecreated(place):
    global desktop_path  
    global number_path
    
    if place == "робочий стіл":
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        number_path = 1
        print(desktop_path)
        
    else:
        number_path = 2
        

    def join_path(desktop_path: str , name_folder) -> str:
        global pathfile
        pathfile = os.path.join(desktop_path,name_folder)
        print(pathfile)
        return pathfile
    
    return join_path 


def askdirs(name_folder: str) -> None:
    Tk().withdraw()
    folder = filedialog.askdirectory(title="виберіть папку")
    os.makedirs(os.path.join(folder, name_folder), exist_ok=True)



def union(place , name_folder):
    if number_path == 1:
        global first_path
        join_path = searchplacecreated(place)
        first_path = join_path(desktop_path , name_folder)
        return first_path
    else: 
        pass


def getftype() -> str:
    from JarvisGeneral.vandcf.File_create.CreaterTk import program , FTYPE #File_create.CreaterTk
    program.mainloop()
    print(FTYPE)
    return FTYPE

def processing(typefile):
    if typefile == "text":
        typefile = "txt"
        return typefile
    else: 
        None

def searchfileplacecreated(place):
    global number_path

    if place == "робочий стіл":
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        number_path = 1
        print(desktop_path)
        return desktop_path
    
    else:
        number_path = 2
        desktop_path = None
        return desktop_path
        


def makefiledesktop(desktop_path: str , name_file , FTYPE):
    name = ".".join([name_file, FTYPE])
    pathfile = os.path.join(desktop_path, name)
    with open(pathfile, "w" , encoding="utf-8") as f:
        f.close()



def makefile(name_file , FTYPE):
    name = ".".join([name_file, FTYPE])
    Tk().withdraw()
    folder = filedialog.askdirectory(title="виберіть папку")
    fullpath = os.path.join(folder, name)
    with open(fullpath, "w", encoding="utf-8") as f:
        f.close()


def cfolder(first_path , name_folder):
    
    if number_path == 1:
        
        os.mkdir(first_path)

    elif number_path == 2:
        askdirs(name_folder)


def cfile(desktop_path , name_file , FTYPE):

    if number_path == 1:

        makefiledesktop(desktop_path , name_file , FTYPE)

    elif number_path == 2:

        makefile(name_file , FTYPE)

