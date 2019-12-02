'''
S11Q02

Write a Python program that takes a file as the first argument 
   and a search word as the second argument. 

This script should print only those lines that have the search word
'''


import sys

a = sys.argv[1]
b = sys.argv[2]


with open (a) as FH:
    fh = FH.readlines()
    for i in fh:
        if b in i:
            print(i)
            
