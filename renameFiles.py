#this script renames ALL! files in the folder you run this script
#first you need to chosse if you want to rename the file names, or rename specific text inside the files
#Then you need to define which text to replace and by what

import os, sys

#Set the file path, filepath is where the .py file is
files_path = os.getcwd()
files_path = os.path.join(files_path, '') #Adds the \\ to the end of the path name

lst = os.listdir(files_path)

print('Hellooo')
print(files_path,"renaming files in here")

#choose:

#--------------------------------------------------------------------------------------------------------------------------------------------
#replace all "old" with "new" in the file's name
 
old = "text1"
new = "text2"
    
for file_name in lst:
    #if file_name.endswith(".png"):
    #if file_name.startsswith("2022_"):
        newname = file_name.replace(old,new)
        os.rename(files_path + file_name, files_path + newname)
        
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#replace all "old" with "new" inside the file 
# old = "text1"
# new = "text2"

# for file_name in lst:   
    # if file_name.endswith(".txt"):
        # f = open(file_name, 'r')
        # filedata = f.read()
        # f.close()

        # newdata = filedata.replace(old,new)
        
        # f = open(file_name,'w')
        # f.write(newdata)
        # f.close()  
   



raw_input('DONE ----- Press ENTER to exit')
