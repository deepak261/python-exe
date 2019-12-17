'''
Write a Python program that takes a file name as its argument. 
This program should count the occurrences of all the words in a file.

   - It should then print the top 10 most repeated words 
        in the descending order of their count.
   - Print a separate list of all the words that
        are not repeated in that file.
'''



import sys

def file(x):
    with open(x) as fl:
        FH = fl.read()
        return FH


def chapter():
    a = "chapter.txt"
    fh = file(a)
    fh = fh.split()
    not_rep = []
    not_repeted = {}
    data = []
    data_1 = {}
    data_2 = {}
    print("The top most frequently occuring words in the file :\n")

    for i in fh:
        strp = i.strip(',')
        strp_1 = strp.strip('.')
        strp_2 = strp_1.strip("'")
        data.append(strp_2.strip())
    
    for i in data:
        if i not in data_1:
            data_1[i] = data.count(i)
    for i in sorted(data_1,key = data_1.get,reverse = 1):
        data_2[i] = data_1[i]
        if int(data_1[i]) == 1:
            not_repeted[i] = data_1[i]
        

    c = 0
    for i,j in data_2.items():
        if c != 10:
            c += 1
            print(str(c)+'.',i,data_2[i],)
        else:
            break
    print("\nThese words are not repeated in the file :\n")
    for i,j in not_repeted.items():
        not_rep.append(i)
    print(not_rep)


#main starts from here
chapter()

