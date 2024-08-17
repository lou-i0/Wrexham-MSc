import turtle
from random import randint

coino = turtle.Turtle()

coins = int(input('Please enter the number of coins you wish to see:'))

print(f'You have elected to print {coins} 50p coins, starting now.')

# create coin for number of coins elected
for i in range(1,coins+1):
    print(f'coin {i}')
    #create coin, 
    for j in range(1,8):
        coino.right(51.43)
        coino.forward(50)
    #pick up pen, find a random position, and pen down     
    coino.penup()
    coino.goto(x = randint(0,300), y = randint(0,300))
    coino.pendown()
        