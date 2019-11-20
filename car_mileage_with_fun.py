'''
 S02AQ01

Re-write the earlier question of S02Q02 using functions :

     - Using the starting and ending values of your car’s odometer, 
            calculate its mileage
'''



def distance(x,y):
    return y-x

def main():
    start = int(input("enter the starting value of odometer:"))
    end = int(input("enter the ending value of odometer:"))
    fuel = 35
    mileage = distance(start,end)//fuel
    print('car mileage:',mileage)

#Main starts from here
main()
