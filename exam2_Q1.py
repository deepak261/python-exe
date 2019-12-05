import random

def seed(x):
    with open (x) as file:
        FH = file.readlines()
        return FH

def slice1(a,start=0,end=10):
    data = ""
    Len = start+end
    with open (a) as file:
        words = ''
        FH = file.read()
        print(FH)
        for i in FH:
            line = i.strip()
            words += line
        f = FH[start:Len]
        if len(f)==50:
            lis = f.split(',')
            random.shuffle(lis)
            print(lis)
            for i in lis:
                data = i+data
            return data
        
    


a='window.txt'
seed(a)
q = slice1(a,0,50)
print(q,len(q))

