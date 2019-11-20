'''
S09Q02

Write a search and replace program in Python. 
This should first take the original text as input by prompting the user for it. 
It should then, prompt the user for which word to search, 
and what new word it should be replaced with.
'''

def user_input():
    x = input("enter the name:")
    return x

m = "write a search and replace program in Python"
print(m)
s = user_input()
search = m.find(s)
print(search)
z = m.replace(s,user_input())
print(z)              
