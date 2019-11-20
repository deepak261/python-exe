'''
S08Q02

Ask the user to enter a number.
- If the number is a single digit number, add 7 to it, 
     and print the number in its unit’s place
- If the number is a two digit number, raise the number to the power of 5, 
     and print the last 2 digits
- If the number is a three digit number, ask user to enter another number. 
     Add the 2 numbers and print the last 3 digits
'''
def user_input():
    d = int(input("Enter the num:"))
    return d

def main():
    x = user_input()
    if x<=9:
        a = x+7
        b = (str(a))
        print(b[-1])
    elif x>9 and x<100:
        y = x**5
        z = (str(y))
        print(z[-2:])
    elif x>99 and x<1000:
        v = user_input()
        add = v+x
        print(str(add)[-3:])

#main starts from here
main()
