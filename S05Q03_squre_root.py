'''
S05Q03

     - Take a number as input from the user. 
           Print all the squares of numbers from 1 to any large number. 
           The numbers printed should be less than 
                 the number given as input by the user

'''


def user_input():
    x = int(input("Enter the user number:"))
    return x

a = user_input()
z = 0
for num in range(1,a):
    z = num*num
    if z<a:
        print(z)

    
