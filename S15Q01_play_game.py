'''
S15Q01

You invited 10 friends to your house to play a game. 
Each one is asked to pick a card that contains a number between 99 and 999. 
The one with the maximum number wins the game. 
Simulate this game using Python
   - Which cards did each one pick ? 
   - Who won the game ?
'''

import random

def sec(x):
    return int(x[1])

def main():
    friends = "deepu basava ravi jogi swami arun vini anil abhi shivu"
    x = random.sample(range(99,999),10)
    frnd_card = []
    print(x)
    print("card pick by each one:")
    y = 0
    friends = friends.split()
    for i in friends:
        name_num = (i+':'+' '+str(x[y]))
        print(name_num)
        y = y+1
        spl=name_num.split()
        frnd_card.append(spl)
        
    frnd_card.sort(key = sec)
    print("winner of the game:")
    print(frnd_card[-1])
    

#main starts from here
main()
