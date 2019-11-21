''''
    S03Q02

     - Ask the user to enter a number.
            - If the number is a single digit number,
                 add 7 to it, and print the number in its unit’s place
            - If the number is a two digit number,
                raise the number to the power of 5, 
                and print the number in its unit’s place
            - If the number is a three digit number, 
                ask the user to enter another number. 
                Add the 2 numbers and print the number in its unit’s place

            Use the solution provided in S03Q01 as the template for this exercises.
            - Instead of doing a print to print the final result in "perform_check" function 
            call separate functions : 
               do_1digit_oper() and
               do_2digit_oper() and
               do_3digit_oper()
            that will perform the required operations based on the number of digits.
'''


def user_input():
    z = int(input("enter the num:"))
    return z

def d0_1digit_oper(f,h):
    return f+h

def d0_2digit_oper(o,p): 
    return o**p

def d0_3digit_oper(q,r):
    return q+r

def main():
    x = user_input()
    if x<=9:
        a = d0_1digit_oper(x,7)
        b = (str(a))
        print(b[-1])
    elif x>9 and x<100:
        c = d0_2digit_oper(x,5)
        d = (str(c))
        print(d[-2:])
    elif x>99 and x<1000:
        v = user_input()
        add = d0_3digit_oper(x,v) 
        print(str(add)[-3:])

#main start from here
main()
    

