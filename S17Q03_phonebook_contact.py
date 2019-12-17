'''
S17Q03 - Phonebook Search Program

Write a Python program that takes a file name as its argument. 
This file contains names of people and their corresponding contact numbers.

- Prompt the user to enter a few characters to search for.
- Print all the names that contain this sequence of characters 
     in the ascending order of their names
'''


import sys


def user_input():
    x = input("Enter a characters : ")
    return x

def file(x):
    with open (x) as file:
        FH = file.readlines()
        return FH


def contact_list():
    count = 0
    c = 0
    fh = file(sys.argv[1])
    user = user_input()
    contact = {}
    lst = []
    for i in fh:
        line = i.split(':')
        contact[line[0]]=line[1]
        user1 = user.title()
        low = user.lower()

    print("Serached result :",user ,"is :\n")
    for key in contact:
        if user1 in str(key):
            a = key+' :'+contact[key]
            lst.append(str(a))
            count += 1
        if count==0:
            if low in str(key):
                a = key+' :'+contact[key]
                lst.append(str(a))
                c += 1
    for i in sorted(lst):
        print(i)
    if count < 1:
        print("Your searched result is not found")
        
   
#main starts from here
contact_list()
