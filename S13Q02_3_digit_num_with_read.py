'''
S13Q02

Create a text file “num.txt” that contains one number per line. 
These numbers can be 1, 2, 3 or 4 digit numbers.

- Write a program to read the numbers from this file
- Discard all numbers that are not 3 digit numbers.
- From all the 3 digit numbers in the file,
    find and print the prime numbers in descending order.
'''



with open ('num.txt') as FH:
    fh = FH.readlines()
    numbers = []
    prime = []
    for line in fh:
        b = len(line.strip())
        if b>2 and b<4:
            numbers.append(int(line.strip()))
    print(numbers)
    for i in numbers:
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            prime.append(i)
    assending=sorted(prime)
    print('assending num is:',assending)
    rever = assending.reverse()
    print('descending num is:',assending)
                
                
           
