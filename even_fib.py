def add(x,y):
    return x+y

def main():
    a = 1
    b = 1
    z = 0
    while True:
        c = add(a,b)
        a = b
        b = c
        if c%2==0:
            print(c)
            z+=1
        if z==12:
            break

#main start from here
main()
