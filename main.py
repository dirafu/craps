import random
def rollDices():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    return a+b, a, b

lucky=[7,11]
unlucky=[2,3,12]
goals=[4,5,6,8,9,10]

validInput = False 
firstroll = True
print("to roll dices enter 'roll'")   
while True:
    while not validInput:
        if input('').lower()=='roll':
            validInput=True
    roll=rollDices()
    if firstroll and (roll[0] in lucky):
        print(f'The sum of dice is {roll[1]}+{roll[2]}={roll[0]}')
        print('You won!')
        break
    elif firstroll and (roll[0] in unlucky):
        print(f'The sum of dice is {roll[1]}+{roll[2]}={roll[0]}')
        print('You lose...')
        break
    elif firstroll and (roll[0] in goals):
        goal = roll[0]
        print(f'The sum of dice is {roll[1]}+{roll[2]}={roll[0]}')
        print(f'Now your goal number is {goal}')
    elif not firstroll and roll[0]==goal:
        print(f'The sum of dice is {roll[1]}+{roll[2]}={roll[0]}')
        print('You won!')
        break
    elif not firstroll and roll[0]==7:
        print(f'The sum of dice is {roll[1]}+{roll[2]}={roll[0]}')
        print('You lose...')
        break
    else:
        print(f'The sum of dice is {roll[1]}+{roll[2]}={roll[0]}')
    firstroll = False
    validInput = False