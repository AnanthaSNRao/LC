'''
Design In-Memory File System
https://algo.monster/liteproblems/588
'''


class TrieNode:
    def __init__(self):
        self.folders = {}
        self.files = []
    
    def addFolder(self, name):
        self.folders[name] = TrieNode()
    
    def addFile(self, file):
        self.files.append(file)
    
    def list(self):
        s = ""
        for f in self.folders:
            s += f + "\n"

        for f in self.files:
            s += f + "\n"
        return s
    
    def search(self, path):
       
        if path == []:
            return self
        elif path[0] in self.folders:
            return self.folders[path[0]].search(path[1:])
        elif len(path) == 1 and path[0] == "":
            return self
        else:
            return None
        
        




class InMemoryFileSys:
    def __init__(self):
        self.root = TrieNode()
    
    def cd(self, path):
        path = path.split("/")

        return self.root.search(path)
    
    def ls(self, path):
        path = path.split("/")

        f = self.root.search(path)
        if f: 
            print(f.list())

    def mkdir(self, path):
        path = path.split("/")
        p = path[:-1]
        f = self.root.search(p)
        if f:
            if "." in path[-1]:
                f.addFile(path[-1])
            else:
                f.addFolder(path[-1])

        return




    
fs = InMemoryFileSys()

fs.mkdir("opt")
fs.mkdir("opt/var")
fs.mkdir("usr")


fs.mkdir("usr/p.txt")
fs.mkdir("usr/arao")
fs.mkdir("usr/arao/resume.pdf")

fs.ls("usr/arao/")
fs.ls("usr/")

fs.ls("")

