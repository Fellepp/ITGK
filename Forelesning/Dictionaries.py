#Oppgave 4)
highscores = {}
highscores[1] = ["Vernon", 100]
highscores[2] = ["Vernon", 100]
highscores[3] = ["Vernon", 100]
highscores[4] = ["Vernon", 100]
highscores[5] = ["Vernon", 100]
highscores[6] = ["Vernon", 100]
highscores[7] = ["Vernon", 100]
highscores[8] = ["Vernon", 100]
highscores[9] = ["Vernon", 100]
highscores[10] = ["Vernon", 100]

#Oppgave 4a)
def check_highscores(points, scores):
    for place in scores:
        if points > scores[place][1]:
            return place
    return -1

#Oppgave 4b)
def print_highscore(scores):
    for x in scores:
        print(str(x).rjust(2), scores[x][0].ljust(20), str(scores[x][1].rjust(5)))

#Oppgave 4c
def add_highscore(points, name, scores):
    place = check_highscores(points, scores)
    if place != -1:
        for x in range(10, place, -1) #Move lower scores down
            scores[x] = scores[x-1] #Kopierer elementet over
            scores[place] = [name, points]
    return scores