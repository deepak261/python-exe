'''
 S01AQ03

     - Modify program in S01Q02 to print the multiplication table 
           of any number desired by the user
'''


def multiply(a,b):
    return a*b

def user_input():
    c = int(input("Enter the number:"))
    return c

def main():
    x = user_input()
    y = 1
    while y <= 10:
        mul = multiply(x,y)
        print(x,'x',y,'=',mul)
        y = y+1

#Main start from here
main()
