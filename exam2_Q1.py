import random

import sys

def seed(x):
    with open (x) as file:
        FH = file.read()
        return FH

def slice1(end=10,start=0,lent=0):
    
    fh = seed(sys.argv[1])
    data = ''
    Len = start + end
    words = ''
    for i in fh:
        line = i.strip()
        words += line
    f = fh[start:Len]
    if len(f) < 50:
        return f
    count = 0
    if len(f) >= 50:
        lis = f.split(' ')
        random.shuffel(lis)
        for i in lis:
            data = i+' '+data
        return data
        

#main starts from here
if __name__=="__main__":
    z = slice1(50)
    print(z)

    
    
    
import window
import sys
def story():

    result = window.slice1(40,15,50)
    fh = open("your_story.txt",'w')
    fh.write(result)
    fh.write('\n')
    fh.write("created by story_maker.py")
    result1 = window.slice1(20,50)
    fh.write('\n')
    fh.write(result1)
    result2 = window.slice1(15)
    fh.write('\n')
    fh.write(result2)
    inpt = input("enter your name")
    fh.write('\n')
    fh.write("copyright")
    fh.write(inpt)
    fh.write("2019.")


#main starts from here
story()

    
