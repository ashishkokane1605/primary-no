#cricket

import random

x=input('enter 1st team name:')
y=input('enter 2nd team name:')
print('TOSS')

def play(team):
    w=0
    sum=0
    while w<6:
        t=random.randrange(1,6)
        if t==5:
            continue
        print(t)
        w=w+1
        sum=sum+t
    print(team,' score',sum)
    return sum
    
        

q=random.randrange(1,2)
n='bat'
m='ball'
if q==1:
    print(x,'won the toss')
    toss=input('bat/ball:')
    if toss=='bat':
        print('play')
        xscore=play(x)
        yscore=play(y)
    if toss=='ball':
        print('play')
        yscore=play(y)
        xscore=play(x)
if q==2:
    print(y,'won the toss')
    toss==input('bat/ball:')
    if toss=='bat':
        print('play')
        yscore=play(y)
        xscore=play(x)
    if toss=='ball':
        print('play')
        xscore=play(x)
        yscore=play(y)

if xscore>yscore:
    print('congratulations.......team',x,'won')
elif xscore<yscore:
    print('congratulations.......team',y,'won')
else :
    print('its a tie')
    


        
