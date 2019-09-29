import random

def tablePrint(table):
    for row in range(0, len(table)):
        s = ""
        for col in range(0, len(table[0])):
            s+=str(table[row][col]).center(5)
        print(s)

def createTable(number, size):
    return [[number for x in range(size)] for y in range(size)]

matrix = createTable(0, 3)
tablePrint(matrix)
print("\n")

def fillTable(table, number):
    start = number
    for i in range(len(table)):
        for j in range(len(table[0])):
            table[i][j] = number
            number += start
    return table

matrixFilled = fillTable(matrix, 2)
tablePrint(matrixFilled)
print("\n")

def sumTable(table):
    sum = 0
    for row in range(len(table)):
        for col in range(len(table[0])):
            sum += table[row][col]
    return sum


matrixSum = sumTable(matrixFilled)
print(matrixSum)
print("\n")

def pickRemoveNumber(list):
    indeks = random.randint(0, len(list)-1)
    tall = list[indeks]
    list.pop(indeks)
    return tall

a = [2, 3, 4, 5]
print(a)
print(pickRemoveNumber(a))
print(a)

