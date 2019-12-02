'''
S14Q03

Ask the user to enter any 10 numbers as input. 
Randomly pick any 5 numbers from this list 
  but print them in the same order as given by the user.
'''



import random

#generating 10 user input random
print("10 user input")
z = random.sample(range(100),10)
print(z)
random_num = []
order_vise = []
count = 1
#randomly pick any 5 numbers
while count <= 5:
    y = random.choice(z)
    count+=1
    random_num.append(y)
print("randomly pick numbers")
print(random_num)
#comparing the between user input to randomly pick numbers
for i in z:
    for j in random_num:
        if i == j:
            #storing the original values in the different list
            order_vise.append(i)
print("storing same order as user input")
print(order_vise)

