'''
S08Q03

Ask the user to enter a number.
- If the user enters a number as 5, then
generate the following string :
- 00001111222233334444

- If the user enters the number as 3, then
generate the following string :
- 001122
'''

x = int(input("Enter a num:"))
for i in range(x):
    a = str(i)*(x-1)
    print(a,end = '')
