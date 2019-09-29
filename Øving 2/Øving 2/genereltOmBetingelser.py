#a)
a = int(input("Skriv inn et tall:"));
b = int(input("Skriv inn enda et tall:"));

if((a*b)>(a+b)):
    print(a+b);
elif((a*b)<(a+b)):
    print(a*b);
else:
    print("Det blir det samme");

#b)
svar = input("Hva blir 3*4?");
if int(svar) == 12:
    print("Korrekt");
else:
    print("Galt");
