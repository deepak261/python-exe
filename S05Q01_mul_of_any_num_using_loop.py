'''
05Q01

- Print the multiplication table of a given number using “for” and “while” loop's.
'''


def user_input():
    x = int(input("Enter the number:"))
    return x

def mul(a,b):
    return a*b

a = user_input()
 
def main():
    for num in range(1,11):
         print(a,'x',num,'=',mul(a,num))

def main1():
    print("multiplication table using while loop")
    b = 1
    while b<=10:
         print(a,'x',b,'=',mul(a,b))
         b=b+1

#main start from here
main()
main1()
    
