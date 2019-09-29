import math

def f(x):
    return (x-12)*math.e**(5*x) - 8*(x+2)**2

def g(x):
    return -x-2*(x**2)-5*(x**3)+6*(x**4)

def derivate(h, x, func):
    f1 = x+h/2
    f2 = x-h/2
    derx = 0

    if func=="f":
        derx = (f(f1)-f(f2))/h
    elif func=="g":
        derx = (g(f1) - g(f2)) / h
    else:
        print("Velg mellom f og g")
    return derx

print(derivate(0.000001, -2, "f"))

def newtons_method(h, x, func, tol):
    differanse = tol+1
    xk1 = x
    while differanse > tol:
        xk = xk1
        if xk1 == xk:
            if(func=="f"):
                xk1 = xk - f(xk)/derivate(h, xk, func)
            else:
                xk1 = xk - g(xk) / derivate(h, xk, func)
        else:
            if(func=="f"):
                xk1 += xk - f(xk)/derivate(h, xk, func)
            else:
                xk1 += xk - g(xk) / derivate(h, xk, func)
        differanse=abs(xk1-xk)
    return xk1

h = float(input("Steglengde: "))
x = float(input("x: "))
func = input("Funksjon: (f/g) ")
tol = float(input("Toleranse: "))

a = newtons_method(h, x, func, tol)
if func == "f":
    print("Funksjonen nærmer seg et nullpunkt når x =", a, ", da er y =", f(a))
elif func=="g":
    print("Funksjonen nærmer seg et nullpunkt når x =", a, ", da er y =", g(a))
else:
    print("Feil funksjon")

