import random

amount = 100
startingBet = 0.01
currentBet = startingBet
goal = 150

numBum = 0

# Testing the win rate of a coin toss strategy where you have a set starting bet and your aim is to get 1.5 times your initial balance by placing the starting bet repeatedly unless the last outcome of the coin toss was a loss, in which case the bet size is doubled.
while numBum < 500:
    numBum += 1
    numFail = 0
    numSucc = 0
    numBets = 0
    while numBets < 500:
        numBets += 1
        amount = 100
        while amount > 0 and amount < goal:
            if random.randrange(2) == 0:
                amount += currentBet
                currentBet = startingBet
            else:
                amount -= currentBet
                currentBet *= 2
            #print(amount)
        if amount > 0:
            #print('fail')
            numFail += 1
        else:
            numSucc += 1
            #print('succ')
    print(numSucc/numFail)