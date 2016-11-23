## Renaming files in your computer ###
# 1. access the files
# 2. for each file, rename the files
import os
def rename_files():
    #1. get file names from a folder
    file_list = os.listdir("/Users/olessiapotapova/Desktop/prank")
    print file_list
    #2. for each file, rename filename
    for filename in file_list:
        print "this is filename: " + filename
        

rename_files()
