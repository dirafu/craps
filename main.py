import random
def rollDices():
    a = random.randrange(1,7)
    b = random.randrange(1,7)
    return a+b, a, b
def printSum(roll):
    print(f'The sum of dice is {roll[1]}+{roll[2]}={roll[0]}')
def run(goal=None, firstroll=False):
    validInput=False
    while not validInput:
        if input('').lower()=='roll':
            validInput=True
    roll=rollDices()
    if firstroll and (roll[0] in lucky):
        printSum(roll)
        print('You won!')
        return goal, True
    elif firstroll and (roll[0] in unlucky):
        printSum(roll)
        print('You lose...')
        return goal, True
    elif firstroll and (roll[0] in goals):
        goal = roll[0]
        printSum(roll)
        print(f'Now your goal number is {goal}')
        return goal, False
    elif not firstroll and roll[0]==7:
        printSum(roll)
        print('You lose...')
        return True
    elif not firstroll and roll[0]==goal:
        printSum(roll)
        print('You won!')
        return True
    else:
        printSum(roll)
        return False
    
lucky=[7,11]
unlucky=[2,3,12]
goals=[4,5,6,8,9,10]

print("to roll dices enter 'roll'")
goal, gameover=run(firstroll=True)
while not gameover:
    gameover=run(goal=goal)
