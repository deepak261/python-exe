'''
S14Q01

Ask user to enter the student’s name followed by his total marks in the SSLC exam. 
An empty line indicates the end of input. 
Print the names and marks of all students 
    who have scored more than 90% marks, 
    in ascending order of their marks.
'''


def user_input():
    name = input("enter the student's name:")
    marks = input("enter the total marks:")
    return name,marks

def sec(x):
    return int(x[1])

def main():
    a_grade = []
    final = []
    while True:
        x,y = user_input()
        if not x or not y:
            break
        else:
            both = x +' '+ y
            grade = both.split()
            a_grade.append(grade)
        print(a_grade)
        
    for line in a_grade:
        if int(line[1]) >= 90:
               final.append(line)
               
    for i in final:
               print(i)
