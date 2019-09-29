for i in range(1,5):
    print(str(i), "- gangen:")
    for j in range(i, i*5, i):
        print(j)

for i in range(2, 100):
    primetall = True
    for j in range(2, int(i**(1/2))):
        if(i%j == 0):
            primetall=False
    if (primetall):
        print(i)

