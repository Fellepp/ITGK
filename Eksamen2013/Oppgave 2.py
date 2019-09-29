#a)
def chess_match():
    total_score1 = 0
    total_score2 = 0

    num_games = int(input("How many rounds are you going to play? "))

    if num_games < 1:
        print("Well, that sucks. I guess there will be no game today")
    else:
        for i in range(0, num_games):
            print("Round:", (i+1))
            score1 = float(input("How many points does player 1 has? "))
            score2 = float(input("How many points does player 2 has? "))
            total_score1 += score1
            total_score2 += score2

    print("The game is over!")
    print("Player 1 got", total_score1, "points")
    print("Player 2 got", total_score2, "points")

chess_match()

#b)
def end_of_match(num_games, game, total_score1, total_score2):
    if total_score1 > (num_games)/2:
        return 1
    elif total_score2 > (num_games)/2:
        return 2
    elif game == num_games:
        return 3
    else:
        return 0

print(end_of_match(6, 1, 2, 2))

#c)
def chess_scorer():
    error = True
    while(error):
        try:
            score1 = float(input("How many points did player 1 get? "))
            if score1 == 0 or score1 == 0.5 or score1 == 1:
                return score1, 1 - score1
            else:
                print("Impossible result")
        except (UnboundLocalError, ValueError):
            print("That's not a number dumbass")

print(chess_scorer())

#d)
res = [1,1,0.5,0,0,None]
def player_score(result):
    num_games = len(result)
    sum = 0
    for i in range(0, num_games):
        if result[i] == None:
            continue
        sum += result[i]
    return sum

print(player_score(res))

