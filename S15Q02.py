import sys


def list1(x):
    lst = []
    with open (x) as file:
        fh = file.readlines()
        for i in fh:
            line = i.strip()
            line_1 = line.strip('')
            line_2 = line_1.split(',')
        for i in line_2:
            line = i.strip()
            lst.append(int(line))
        return lst
                
a = list1(sys.argv[1])
b = list1(sys.argv[2])
c = a+b
new_list = []
x = 0
maximum = max(c)
for i in range(int(maximum+1)):
    for j in c:
        if i == j:
            new_list.append(j)
            x += 0
print("left list :",a)
print("right list :",b)
print("combined of both list in sorted order :")
print(new_list)
   
