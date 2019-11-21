'''
S04Q02

     - Brilliant School sets an exam wherein, 
                English exam is for 80 marks, 
                Science for 90 marks and 
                Mathematics for 100 marks. 

            Ask the student to enter the marks scored in each of these exams. 
            Calculate the total percentage marks and rank the student as below :
               - First Class if score is more than or equal to 90 %
               - Second Class if score is more than or equal to 75%
               - Average if student has not failed
               - Failed if score is less than or equal to 35 %
'''

def per(a,b):
    z = (a/b)*100
    return z

def add(a,b,c):
    return a+b+c
 
ep = int(input("Enter eng max marks is 80:"))
sp = int(input("Enter sci max marks is 90:"))
mp = int(input("Enter maths max marks is 100:"))

total = add(ep,sp,mp)
total_per = per(total,270)
print('Total percentage:',total_per,'%')

if ep>27 and sp>32 and mp>35:
    if ep<=80 and sp<=90 and mp<=100:
        if total_per>=90 and total_per<=100:
            print("Rank:First class")
        elif total_per>=75 and total_per<90:
            print("Rank:Second class")
        elif total_per<=35 and total_per<75:
            print("Rank:Failed")
        else:
            print("Rank:Average")
else:
    print("Rank:fail")
