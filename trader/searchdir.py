import os, re

pattern = '[gG]itBackup'
root_dir = r'D:/'

isFind = False

for self_dir, subdirs, files in os.walk(root_dir):
    if re.search(pattern,self_dir):
        print(self_dir)
        #isFind=True
    for dir in subdirs:
        if re.search(pattern,dir):
            print(dir)
            #isFind=True

    #if isFind:
    #    break
        


    
