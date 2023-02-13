#Python script to check, if the number of files on R:/ are the same as lines in the MD5

#Paths
import os, sys
from os import remove
from sys import argv

parent = os.getcwd()
                    #print ("main folder = ", parent)


raw_input('Press ENTER')


#number of lines in MD5
fileMD5x = parent[-17:]
fileMD5 = fileMD5x+'_MD5.xml'
                    #print ("MD5 name = ", fileMD5)
pathMD5 = parent+'\\'+fileMD5
                    #print ("MD5 path = ", pathMD5)

count = len(open(pathMD5).readlines(  ))
                    #print ("MD5 lines = ", count)


#number of files on R:/
count2 = 0
for root_dir, cur_dir, files in os.walk(parent):
    count2 += len(files)
        
count2 = count2-1
        
                     #print('File count on R:', count2)

#bring it togehter
A = (count-3)/9
C = count2-1

print ("A = ", A, "     C = ", C)

raw_input('DONE ----- Press ENTER to exit')
os.remove(sys.argv[0])