'''
S12Q01

Write a search and replace program in Python. 
This should prompt the user for which word to search,
  and what new word it should be replaced with. 

The file to be modified should be taken as argument to this program
'''


import sys
a = sys.argv[1]

with open (a) as FH:
    fh = FH.readlines()
    x = input("Enter the search world")
    y = input("Enter the replace world")
    with open (a,'w') as file:
        for i in fh:
            if x in i:
                replace = i.replace(x,y)
                file.write(replace)
            else:
                file.write(i)
              
    
        
