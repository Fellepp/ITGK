import random
øvreGrense = int(input("Skriv inn øvre grense"))
random_number = random.randint(1, øvreGrense)
antallGjetninger = 0
galtSvar = True

while(galtSvar):
    if antallGjetninger > 0:
        print("That was your " + str(antallGjetninger) + ". try")
    svar = int(input("Make a guess "))
    antallGjetninger += 1
    if svar == random_number:
        print("You guessed correct! The number was", random_number)
        print("You tried ", antallGjetninger, "times")
        galtSvar = False
    elif svar > random_number:
        print("You guessed", svar, "but the correct number is lower")
    elif svar < random_number:
        print("You guessed", svar, "but the correct number is higher")