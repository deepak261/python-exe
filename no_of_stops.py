'''
S02Q02

     - Using the starting and ending values of your car’s odometer, 
            and the measure of fuel consumed, 
            calculate the number of stops one should make for refuelling 
            while travelling from Bangalore to Goa, 
            a distance of 560 kms.
'''



start = int(input("enter the starting value of odometer "))
end = int(input("enter the ending value of odometer "))
distance = end-start
tank_capacity = 20
car_mileage = 17
fuel = (distance//car_mileage)
print('fuel:',fuel,'liters')
stops = (fuel//tank_capacity)
print('no of stops:',stops)
print('total distance:',distance,'kms')
