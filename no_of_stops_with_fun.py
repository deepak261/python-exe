'''
 S02AQ02

Re-write the earlier question of S02Q02 using functions :

     - Using the starting and ending values of your car’s odometer, 
            and the measure of fuel consumed, 
            calculate the number of stops one should make for refuelling 
            while travelling from Bangalore to Goa,
'''




def distance(x,y):
    return y-x

def main():
    start = int(input("enter the starting value of odometer:"))
    end = int(input("enter the ending value of odometer:"))
    mileage = 17
    tank_capacity = 20
    fuel = distance(start,end)//mileage
    print('fuel:',fuel,'liters')
    stops = fuel//tank_capacity
    print('no of stops:',stops)
    print('distance:',distance(start,end),'kms')

#Main starts from here
main()
