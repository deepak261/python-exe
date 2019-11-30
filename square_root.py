
def user_input():
    x = int(input("enter the num:"))
    return x

def main():
    num = 1
    while True:
        num = user_input()
        if num==0:
            break
        elif num>99 and num<1000:
            print('squre root of num:',num*num)
        else:
            continue

#main starts from here
main()
