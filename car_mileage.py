'''
S02Q01

     - Using the starting and ending values of your car’s odometer, 
            calculate its mileage
'''



start = int(input("enter the starting value of odometer "))
end = int(input("enter the ending value of odometer "))
fuel = 35
mileage = (end-start)//fuel
print('mileage:',mileage)
