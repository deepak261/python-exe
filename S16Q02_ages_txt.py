'''
S16Q02

Write a Python program that prompts the user for a file. 
This file contains names of people and their ages. 

Read the file, and print the list with the oldest person’s name listed first. 
A sample file [ AGES.TXT ] is shown above :
'''


def user_input():
    x = input("enter the file name:")
    return x

def sec(x):
    return int(x[1])


a = user_input()

age = dict()
name_age = []

with open (a +".txt") as file:
    fh = file.readlines()
    age = dict()
    for i in fh:
        a = i.strip()
        line = a.split('-')
        name_age.append(line)
    name_age.sort(key = sec)
    print("sorted based on age in assending order")
    for j in name_age:
        print(j)
        age[j[0]]=int(j[1])
    
    for i in sorted(age,key=age.get,reverse=1):
            print(i+'-',age[i])
