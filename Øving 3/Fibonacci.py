f0 = 0
f1 = 1
fk = 0
sann = True
teller = 0
sum = 1
k = int(input("Hva er det k-te fiboaccitallet f(k) du vil ha ut?"))
while(sann):
    if k==0:
        fk = 0
        sum = 0
        break
    elif k==1:
        fk = 1
        break
    fk = f0+f1
    f0=f1
    f1=fk
    sum += fk
    print(teller)
    teller = teller + 1
    print(f0, f1, fk)
    if teller==k-1:
        sann = False
print("Det k-te fibonaccitallet er,", fk, "Summen er", sum)

#Modifisert
f0 = 0
f1 = 1
fk = 0
sann = True
teller = 0
fklist = [0, 1]
k = int(input("Hva er det k-te fiboaccitallet f(k) du vil ha ut?"))
while(sann):
    if k==0:
        fk = 0
        break
    elif k==1:
        fk = 1
        break
    fk = f0+f1
    f0=f1
    f1=fk
    fklist.append(fk)
    teller = teller + 1
    if teller==k-1:
        sann = False
print(fklist)



