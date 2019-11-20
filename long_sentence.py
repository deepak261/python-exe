'''
S07Q03

Prompt the user to enter a long sentence
        - What is the last character in the sentence ?
        - What are the last 5 characters in the sentence ?
        - Print the characters that are present in 2nd and 5th position of the sentence
        - Print the character at the center of the string, along with the 2 adjoining characters. 
        Ex : If the string entered is "Web Browser”
        the character at its centre is "r" and so print "Bro"
'''

a = input("enter the sentence :")
b = len(a)
print(a[-1:])
print(a[-5:])
print(a[2],a[5])
x = b//2
y = (x+1)
z = (x-1)
print(a[z]+a[x]+a[y])

