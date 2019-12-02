'''
S10Q01

Get the name of the text file from the user. 
Check if all the sentences in that text file begin with a capital letter.
'''

def user_input():
    x = input("enter the file name:")
    return x

a = user_input()

with open (a + ".txt") as FH:
    fh = FH.readlines()
    for i in fh:
        if i[0].isupper():
            print(i)
        

