'''
S11Q01

From a file that contains a list of numbers.
Find the maximum number in that list. 
Also find the sum of all the numbers in that list.
'''


with open ("num.txt") as FH:
    fh = FH.readlines()
    data = []
    for i in fh:
        a = i.strip('\n')
        data.append(int(a))
    print('maximum:',max(data))
    print('minimum:',min(data))
    print('sum:',sum(data))
    
    
