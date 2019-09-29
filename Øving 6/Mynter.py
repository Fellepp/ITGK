import math

def count_coins(coins):
    return sum(coins)

coins = [20, 10, 1, 1,5, 10]
print(count_coins(coins))

def num_coins(numbers):
    coins = []
    for i in range(0, len(numbers)):
        value = numbers[i]
        twentys = math.floor(value/20)
        value = value - twentys*20
        tens = math.floor(value/10)
        value = value - tens*10
        fives = math.floor(value/5)
        value = value - fives*5
        ones = math.floor(value/1)
        NumberOfCoins = [twentys, tens, fives, ones]
        coins.append(NumberOfCoins)
    return coins

numCoins = [12,23,34,45,56,67,78,89,90,98,87,65,54,43,21]
print(numCoins)
print(("20's, 10's, 5's, 1's: \n"), num_coins(numCoins))

def check_weights(numbers):
    coinWeight = [9.9, 6.8, 7.85, 4.35]
    weightList = []
    coins = num_coins(numbers)
    for i in range(0, len(coins)):
        weight = 0
        for j in range(0, 4):
            weight += coins[i][j] * coinWeight[j]
        weightList.append(round(weight, 2))
    return weightList
print(check_weights(numCoins))



