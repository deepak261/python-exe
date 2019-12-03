'''
Write a Python program that takes a file name as its argument. 
This file contains names of people and their corresponding contact numbers. 

Read the file, and print the list in the ascending order of their names. 
A sample file [ CONTACT_LIST.TXT ] is shown below :
'''


import sys

a = sys.argv[1]

contact=dict()

with open (a) as file:
    fh = file.readlines()
    for i in fh:
        line = i.split(':')
        contact[line[0]]=int(line[1])

    for key in sorted(contact):
        print(key+':',contact[key])
