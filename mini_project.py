

def user_input():
    a = int(input("enter your passcode : "))
    return a



def main():
    print("your input should be less then 25")
    y = 12
    c = 0
    count = 0
    counting = 0
    while counting < 4:
        x = user_input()
        
        if x >=(y-2) and x < y or x > y and x <= (y+2):
            print("InVaLiD PaSsCoDe")
            count += 1
        elif x < (y-2) and c < 2:
            print("invalid passcode")
            c = c + 1
        elif x > (y+2) and x <= 25 and c < 2:
            print("INVALID PASSCODE")
            c = c + 1
        elif  c == 2 and :
            print("Login FAILED !!!")
            break
        elif x > (y+2) and x <= 25 and c == 3:
            print("Login FAILED !!!")
            break
        
        elif x > 25:
            print("you reached the maximumu limit of input, It should be less then : 25 :")
            break
        elif x == y:
            print("WELCOME !!!")
            break
        counting += 1

    while count >= 3:
        print("This is your last chance please enter your correct passcode")
        x = user_input()
        if x == y:
            print("WELCOME !!!")
            c = c + 1
            break
        else:
            print("Login FAILED !!!")
            c = c + 1
            break

main()
