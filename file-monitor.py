import os
import time
from time import sleep

print('Starting program')

filesExistBool = 0
files = []

while True:
    print()
    print()
    print()
    
    # - List the current files:
    del files
    files = os.listdir("C:\TestFolder")
    print('Files in the directory:')
    for i in files:
        print(i)
    
    # - Determine filesExistBool:
    if len(files) > 0:
        filesExistBool = 1
    else:
        filesExistBool = 0
    
    # - Save the state to a file:
    saveFile = open('./filesExistBool.txt', 'w')
    saveFile.write(str(filesExistBool))
    saveFile.close()

    print()
    print('Files exist =', filesExistBool)
    sleep(1)
    