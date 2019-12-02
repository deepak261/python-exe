'''
S13Q01

Ask the user to enter a 3 digit number, till he enters 0. 
Discard all numbers that are not 3 digit numbers. 
From all the 3 digit numbers entered by the user, 
     find and print the prime numbers in descending order.
'''


def user_input():
    x = int(input("enter the num:"))
    return x

a = 1
numbers = []
prime  = []
while a != 0:
    a = user_input()
    b = len(str(a))
    print(b)
    if b>=3 and b<4:
        numbers.append(a)
        print(numbers)
for i in numbers:
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        prime.append(i)
assending=sorted(prime)
print('assending num is:',assending)
rever = assending.reverse()
print('descending num is:',assending)
            
            
        
        
