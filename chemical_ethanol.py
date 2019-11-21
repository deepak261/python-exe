'''
S04Q01

     - A Chemical plant has a tank for storing ethanol.
            - When the tank is more than 80% full, it
                 should raise an alarm to close the valve.
            - When the tank is less than 20% full, it
                 should send an SMS to buy more liquid.
            - The total tank capacity is 900 litres.
            - Write a program to simulate this.
            - Ask user to enter current level of ethanol in the tank.
            - Print the appropriate action based on value entered
            - Make sure that your program needs minimum changes
                 for a tank of different capacity.
'''

def user_input():
    x = int(input("Enter level of ethanol in the tank:"))
    return x

def per(a,b):
    z  = (a/b)*100
    return z


p = per(user_input(),900)
print('Present tank liquid percentage is:',p,'%')
if p>80:
    print("close the valve")
elif p<20:
    print("buy more liquid")
else:
    print("no need to fill the tank")
    
