def oppga(tol):
    prod0 = 1
    prod = 0
    teller = 1

    while(prod0-prod > tol):
        if prod == 0:
            prod = 1+(1/(teller**2))
        else:
            prod *= 1+(1/(teller**2))
        print(teller)
        teller += 1
        prod0 = (1+(1/(teller**2))) * prod
        print(prod, prod0)
        print()
    return round(prod0,2), teller

tol = float(input("Skriv inn en toleranse: "))
print("Prod/Count", oppga(tol))