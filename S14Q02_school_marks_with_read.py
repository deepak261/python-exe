'''
S14Q02

Create a text file called “students.txt”. 
Each line should be of the form
“student_name : student_marks”

- Write a Python program to read the contents from this file.
- Print the names and marks of all students 
      who have scored more than 90% marks, 
      in ascending order of their marks.
'''

def user_input():
    name = input("enter the student's name:")
    marks = input("enter the total marks:")
    return name,marks

def sec(x):
    return int(x[1])

with open ('students.txt') as file:
    FH = file.readlines()
    a_grade = []
    for line in FH:
        slp_line = line.strip()
        print(slp_line)
        slp_line = slp_line.split(':')
        if int(slp_line[1])>=90:
               a_grade.append(slp_line)
    for i in a_grade:
               print(i)
    a_grade.sort(key = sec)
    print("sorted student marks list")
    for i in a_grade:
               print(i)
               
