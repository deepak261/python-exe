'''
S05Q02

     - Ask the user to enter a number till he enters 0. 
          Print the maximum and minimum values among all entered numbers. 
          Print the number of single, two and three digit numbers entered.
'''

def user_input():
    x = int(input("enter the number:"))
    return x

a = user_input()
maximum = a
minimum = a

while a!=0:
    a = user_input()
    z = len(str(a))
    if a==0:
        break
    else:
        if a>=maximum:
            maximum = a
        if a<=minimum:
            minimum = a
        if z==1:
            print("single_digit")   
        elif z==2:
            print("two_digit")
        elif z==3:
            print("Three_digit")
        
print('max:',maximum)
print('min:',minimum)       
    
    
