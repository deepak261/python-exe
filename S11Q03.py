'''
S11Q03

Write a Python script that takes a file name as its first argument. 
Create a copy of the contents of this file satisfying the following conditions :
   
   - If the file name is “file.txt”,
       then the name of the new file should be “file-new.txt”
   - Every even line of the first file, should be
       repeated in the new file.
   - The first line of the first line, should be
       repeated after the last line of the first file.
   - A sample input and output file is shown below
'''


import sys
a = sys.argv[1]

with open (a) as FH:
    fh = FH.readlines()
    b = a.strip('.txt')
    b = b+'-file.txt'
    with open (b,'w') as file:
        count = 0 
        for i in fh:
            count = count+1
            if count%2 == 0:
                file.write(i)
                file.write('\n')
                file.write(i)
                file.write('\n')
            else:
                file.write(i)
                file.write('\n')
        file.write(fh[0])
        
        
