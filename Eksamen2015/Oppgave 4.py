import random

# a)
NTNU_scores = (89, 77, 65, 53, 41, 0)
NTNU_letters = ("A", "B", "C", "D", "E", "F")
TASKS = ("1", "2a", "2b", "2c", "3a", "3b", "3c", "3d", "4a", "4b", "4c", "4d", "4e", "4f", "4g", "4h")
WEIGHTS = tuple([25] + (15 * [5]))

print(NTNU_scores)
print(NTNU_letters)
print(TASKS)
print(WEIGHTS)
print("\n")


# b)
def makeArray(numbers, text):
    limitLetters = []
    for i in range(0, len(numbers)):
        limitLetters.append([numbers[i], text[i]])
    return limitLetters


limitLetters = makeArray(NTNU_scores, NTNU_letters)
weightTasks = makeArray(WEIGHTS, TASKS)
print(limitLetters)
print(weightTasks)


# c)
def computeScore(points, weights):
    scores = 0
    for i in range(0, len(points)):
        scores += points[i] * weights[i]
    scores = scores / 10
    return scores


score1 = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
score2 = [10, 0, 0, 0, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0]
score3 = [5, 0, 0, 0, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0]
score4 = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
print(computeScore(score1, WEIGHTS))
print(computeScore(score2, WEIGHTS))
print(computeScore(score3, WEIGHTS))
print(computeScore(score4, WEIGHTS))


# d)
def score2Letter(scoreSum, limitLetters):
    grade = ""
    for i in range(len(limitLetters) - 1, 0 - 1, -1):
        if scoreSum >= limitLetters[i][0]:
            grade = limitLetters[i][1]
    return grade


print(score2Letter(88.9, limitLetters))


# e)
def addCandidate(candidateNumber, scores, weights):
    write = ""
    write += str(candidateNumber) + "\t"
    for i in range(len(scores)):
        write += str(scores[i]) + "\t"
    write += str(round(computeScore(scores, weights), 1)) + "\n"
    try:
        with open("eksamen.txt", "a+") as f:
            f.write(write)
    except Exception as errorMessage:
        print(errorMessage)


def pointMaker():
    points = []
    for i in range(len(TASKS)):
        points.append(random.randint(0, 10))
    return points


"""addCandidate(12345,pointMaker(),WEIGHTS)
addCandidate(12346,pointMaker(),WEIGHTS)
addCandidate(12392,pointMaker(),WEIGHTS)
addCandidate(12212,pointMaker(),WEIGHTS)
addCandidate(12321,pointMaker(),WEIGHTS)
addCandidate(12397,pointMaker(),WEIGHTS)
addCandidate(12390,pointMaker(),WEIGHTS)
addCandidate(12393,pointMaker(),WEIGHTS)"""


# f)
def readResultFile(filename):
    table = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            line = line.split("\t")
            #line = line.split()
            table.append(line)
    return table


table = readResultFile("eksamen.txt")
for line in table:
    print(line)


# g)
def checkResultOK(filename, weights):
    error1 = False
    can1 = ""
    error2 = False
    can2 = ""
    error3 = False
    can3 = ""

    table = readResultFile(filename)

    candidateList = []

    for i in range(0, len(table)):
        candidateList.append(table[i][0])
        for j in range(1, len(table[0]) - 1):
            if int(table[i][j]) > 10 or int(table[i][j]) < 0:
                error2 = True
                can2 = table[i][0]

        scores = table[i][1:len(table[0]) - 1]
        for s in range(0, len(scores)):
            scores[s] = int(scores[s])

        if float(table[i][len(table[0]) - 1]) != computeScore(scores, weights):
            error3 = True
            can3 = table[i][0]

    for i in range(0, len(candidateList)):
        if candidateList.count(table[i][0]) > 1:
            error1 = True
            can1 = candidateList[i]

    if error1 or error2 or error3:
        if error1:
            print("Candidate", can1, "appears more than once!")
        if error2:
            print("Candidate", can2, "scores are not between 0-10!")
        if error3:
            print("Candidate", can3, "has wrong total score!")
    else:
        return True


#print(checkResultOK("eksamen.txt", WEIGHTS))


# h)
def listAll(filename, limitLetters):
    table = readResultFile(filename)
    """for i in range(0, len(table)-1):
        if table[i][0] > table[i+1][0]:
            temp = table[i]
            table[i] = table[i+1]
            table[i+1] = temp"""
    table.sort()
    for i in range(0, len(table)):
        nr = table[i][0]
        scoreSum = table[i][len(table[0]) - 1]
        grade = score2Letter(float(scoreSum), limitLetters)
        print(nr.ljust(5) + scoreSum.rjust(10) + grade.rjust(3))
    return len(table)


print(listAll("eksamen.txt", limitLetters))
