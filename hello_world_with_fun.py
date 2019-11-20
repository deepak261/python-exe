'''
S01AQ01

Re-write the earlier question of S01Q01 using functions as mentioned below :

           You can use following code template to create your solution : https://git.io/vgrjP
           [ Click on "RAW" button if you find it difficult to download the code ]

  - Modify the first “Hello World” program to prompt for user’s name 
           and then wish the user by saying Hello followed by his name

           Example :
           If user's name is Sam, then expected output is :
           Hello Sam !!!
'''


def user_input():
    user_input = input('enter the name:')
    return user_input


def main():
    name = user_input()
    print("hello",name)
    

#main program start here

main()
