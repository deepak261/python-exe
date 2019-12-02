'''
S10Q03

Write a Python script that takes a file name as its argument. 
Write the contents of this file to another file such that, 
   each sentence is stored on a new line.
'''

import sys

a = sys.argv[1]

with open (a) as FH:
    fh = FH.read()
    data = fh.split('.')
    with open ('new_file.txt','w') as file:
        for i in data:
            file.write(i)
            file.write('\n')
        
