def per(a,b):
    c = (a/b)*100
    return c

def add(x,y,z):
    return x+y+z

def main():
    e = int(input("Enter eng max marks is 75:"))
    st =int(input("Enter sci theory max marks is 75:"))
    sp = int(input("Enter sci practical max marks is 25:"))
    m = int(input("Enter maths max marks is 100:"))
    s = st+sp
    print('sci marks:',s)
    total_marks = add(e,s,m)
    total_per = per(total_marks,275)
    print('total marks:',total_marks)
    print('total per:',total_per,'%')

    if e>=25 and s>35 and m>=35:
        if e<=75 and s<=100 and m<=100:
            if total_per>=90 and total_per<=100:
                print("Grade A")
            elif total_per>=75 and total_per<90: 
                print("Grade b")
            else:
                print("average")
    else:
        print("fail")

#main starts from here
main()
