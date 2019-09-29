#a)
def newVector():
    vektor = [float(i) for i in input("Skriv inn vektor: ").split(",")]
    return vektor

vec1 = newVector()

#b)
def printOut(vec1):
    print("vec1 =", vec1)

#c)
def skalarDef(vec1, skalar):
    vec2 = list(vec1)
    for i in range(0, len(vec1)):
        vec2[i] *= skalar
    return vec2

#d)
def vecLengde(vec1):
    lengde = 0
    for i in range(0, len(vec1)):
        lengde += vec1[i]**2
    lengde = lengde**0.5
    return lengde

#e)
def indreproduktet(vec1, vec2):
    sum = 0
    for i in range(0, len(vec1)):
        sum += vec1[i]*vec2[i]
    return sum




printOut(vec1)
skalar = int(input("Skriv inn skalar: "))
print(skalarDef(vec1, skalar))
print("Lengde:", vecLengde(vec1), "lengde etter skalar:",
      vecLengde(skalarDef(vec1, skalar)), "Vec1 =",
      vecLengde(vec1)/vecLengde(skalarDef(vec1, skalar)), "* Vec2")
vec3 = newVector()
print(indreproduktet(vec1, vec3))