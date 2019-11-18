'''
S01Q03

     - Modify program in S01Q02 to print the multiplication table 
           of any number desired by the user
'''



x = int(input("enter the number : "))
y = 1
while y <= 10:
    print(x,'x',y,'=',x*y)
    y = y+1
    
