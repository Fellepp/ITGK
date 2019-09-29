#a)
"""r = float(input("Skriv inn en r: "))
n = int(input("Den geometriske rekken går fra 0-n, vennligst gi en n: "))

sum = 0.0
fortsett = 0
while(fortsett<=n):
    sum += r**(fortsett)
    fortsett+=1

print("Summen av rekken er", sum)"""

#b og c)
r = float(input("Skriv inn en r: "))
tol = float(input("Skiv inn en toleranse: "))

sum = 0.0
teller = 0
forsett = True
grenseverdi = 1/(1-r)
while grenseverdi-sum >= tol:
    sum += r**(teller)
    teller +=1

differanse = grenseverdi - sum
print("For å være innafor toleransegrensen:", tol, ", kjørte løkken",
      teller, "ganger")
print("Differansen mellom virkelig og estimert verdi var da ", differanse)
