#a)
sann = True
while(sann):
    tall = 120
    from turtle import *
    # importerer funksjoner fra turtle
    print("Hei, jeg kan tegne en trekant")
    svar = input("Ønsker du spissen på trekanten opp eller ned (O / N)? ")
    svar1 = input("Velg pennfarge, NTNU-rosa (R) eller NTNU-turkis (T)" )
    svar2 = input("Velg fyllfarge, NTNU-gul (G), NTNU-oransje (O) eller NTNU-brun (B)" )
    if svar == "N":
        tall = -120
    if svar1 == "R":
        pennfarge = "#ad208e";
    elif svar1 == "T":
        pennfarge = "#5cbec9";
    if svar2 == "G":
        fyllfarge = "#f1d282"
    elif svar2 == "O":
        fyllfarge = "#f58025"
    elif svar2 == "B":
        fyllfarge = "#90492d"
    pensize(7)          # sett pennen 7 piksler tykk
    pencolor(pennfarge)    # sett pennefargen til rosa
    bgcolor("grey")     # sett bakgrunnsfargen grå
    fillcolor(fyllfarge) # sett fyllfargen lilla
    # Tegner en fylt trekant
    begin_fill()
    forward(200)        # gå 100 piksler framover
    left(tall)           # drei 120 grader venstre
    forward(200)  
    left(tall) 
    forward(200)
    end_fill()
    sjekk = input("Fortsette? (y/n) ")
    if sjekk == "n":
        sann = False
