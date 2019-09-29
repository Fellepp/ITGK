#a
def separate(numbers, threshold):
    biggerThan = []
    lessThan = []
    for i in numbers:
        if numbers[i] < threshold:
            lessThan.append(numbers[i])
        else:
            biggerThan.append(numbers[i])
    return lessThan, biggerThan

lst = range(0, 6)
print(separate(lst, 4))

#b
def multiplication_table(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = (i+1)*(j+1)
    return matrix

def matrixPrint(lst, n):
    matrix = multiplication_table(n)
    for i in range(0, len(matrix)):
        print(matrix[i])

matrixPrint(lst, 100)