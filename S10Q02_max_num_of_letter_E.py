'''
S10Q02

Write a Python script that takes a file name as its argument. 
In that file, find the line that has the maximum number of 
occurrences of the letter ‘e’
'''


import sys

a = sys.argv[1]

with open (a) as FH:
    fh = FH.readlines()
    count = 0
    line = 0 
    for i in fh:
        a = i.count('e')
        print(i,'=',a)
        if a >= count:
            count = a
            line = i
    print(line)
