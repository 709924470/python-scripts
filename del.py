import os,shutil
file = os.getcwd() + '\\'
folders = []

def dirlist(path, delete):  
    filelist =  os.listdir(path)  
  
    for filename in filelist:  
        filepath = os.path.join(path, filename)  
        if os.path.isdir(filepath) and len(os.listdir(filepath)) != 0:  
            dirlist(filepath, delete)
        elif os.path.isdir(filepath):
            delete.append(filepath)
    return delete

def start():
    folders = []
    dirlist(file,folders)
    for dl in folders:
        print("Deleting "+dl)
        shutil.rmtree(dl)

if __name__ == "__main__":
    while len(folders) != 0:
        start()