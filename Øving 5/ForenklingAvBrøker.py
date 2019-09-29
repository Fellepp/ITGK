def gcd(a, b):
    while b!=0:
        gammel_b=b
        b = a%b
        a=gammel_b
    return a

def reduce_fraction(a, b):
    d = gcd(a, b)
    var1 = a/d
    var2 = b/d
    return var1, var2

x, y = reduce_fraction(5, 10)
print(x, "/", y)

x, y = reduce_fraction(4, 2)
print(x, "/", y)

x, y = reduce_fraction(42, 13)
print(x, "/", y)