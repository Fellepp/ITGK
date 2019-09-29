import random


# a)
def check_highscore(points, scores):
    for keys in scores:
        if scores[keys][1] < points:
            return keys
    return -1


# b)
def print_highscores(scores):
    for keys in scores:
        print(str(keys).rjust(2), str(scores[keys][0]).ljust(20), str(scores[keys][1]).rjust(5))


# c)
def add_highscore(points, name, scores):
    ranked = check_highscore(points, scores)
    lastPlace = 10
    if ranked == -1:
        return scores
    else:
        for keys in range(lastPlace, ranked, -1):
            scores[keys] = scores[keys - 1]
        scores[ranked] = [name, points]
    return scores


# d)
def most_highscores(scores):
    lead = ""
    leadCounter = 1
    for keys in scores:
        counter = 0
        checking = scores[keys][0]
        for i in range(keys, 11):
            if scores[i][0] == checking:
                counter += 1
        if counter > leadCounter:
            leadCounter = counter
            lead = checking
    return lead


# e)
def new_highscore():
    dict = {}
    for i in range(1, 11):
        dict[i] = ["", 0]
    names = ["Albus", "Fleur", "Frank", "Harry", "Hermine", "Minerva", "Ron", "Severus", "Sirius", "Vernon"]
    for i in range(0, len(names)):
        add_highscore(random.randint(1, 10)*10, names[i], dict)
    return dict


highscores = new_highscore()
print(highscores)
print()

print(check_highscore(10, highscores))
print()

print_highscores(highscores)
print()

print_highscores(add_highscore(65, "Luna", highscores))
print()

print(most_highscores(highscores))
