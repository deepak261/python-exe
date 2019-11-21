'''
S03Q01

     - Take 2 numbers from the user. 
            Print which number is a 2 digit number, 
            and which number is a 3 digit number. 
            If it is neither, then print the number as it is
'''


x = int(input('enter the num:'))
y = int(input('enter the num:'))
if (x>9 and x<100):
    print("x:two_digit")
elif(y>9 and y<100):
    print("y:two_digit")
if (x>99 and x<1000):
    print("x:three_digit")
elif(y>99 and y<1000):
    print("y:three_digit")
else:
    print(x,y)
    
