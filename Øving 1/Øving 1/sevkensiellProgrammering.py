Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 5*12+6-1
65
>>> 5*2-4
6
>>> 5.5+4.5
10.0
>>> 1+2*(-3)
-5
>>> 5:2-4
SyntaxError: illegal target for annotation
>>> 5/2-4
-1.5
>>> 4((5+3)/2+7)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    4((5+3)/2+7)
TypeError: 'int' object is not callable
>>> 4((5+3)/2+7)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    4((5+3)/2+7)
TypeError: 'int' object is not callable
>>> 4((5+3)/(2) + 7)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    4((5+3)/(2) + 7)
TypeError: 'int' object is not callable
>>> ((5+3)/2+7) * 4
44.0
>>> ((3+5*2)+1)/2
7.0
>>> 245//60
4
>>> 245%60
5
>>> 79//24
3
>>> 79%24
7
>>> 80//7
11
>>> 80%7
3
>>> (-3)**2+5*3-7
17
>>> -3
-3

>>> -3**2+5*3-7
-1
>>> (-4)**-3+5(3-7/2)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    (-4)**-3+5(3-7/2)
TypeError: 'int' object is not callable
>>> (-4)**-3+5*(3-7/2)
-2.515625
>>> 2**2+4
8
>>> 2**2/4
1.0
>>> print("Jeg er student")
Jeg er student
>>> print("Trondheim er Norges beste studisted")
Trondheim er Norges beste studisted
>>> print("I love python")
I love python
>>> print("2+2 = 5")
2+2 = 5
>>> print("2+3 = 5")
2+3 = 5
>>> print('Hvis jeg gjør riktig nå, øker sannsynligheten for at studassen min sier: "Øvingen er godkjent"')
Hvis jeg gjør riktig nå, øker sannsynligheten for at studassen min sier: "Øvingen er godkjent"
>>> a = 2
>>> b = 3
>>> x = 0.5
>>> y = 0.7
>>> a**4+b/y+4*x
22.285714285714285
>>> 0.3x-a**-b/y+8
SyntaxError: invalid syntax
>>> 0.3*
SyntaxError: invalid syntax
>>> 0.3*x-a**-b/y+8
7.9714285714285715
>>> input("Fornavn?")
Fornavn?Ola
'Ola'
>>> input("Etternavn?")
Etternavn?Nordmann
'Nordmann'
>>> fornavn = input("Fornavn?")
Fornavn?Ola
>>> etternavn = input("Etternavn?")
Etternavn?Nordmann
>>> alder = input("Alder (år)?")
Alder (år)?40
>>> print(fornavn, etternavn, 'er', alder, 'år gammel.')
Ola Nordmann er 40 år gammel.
>>> 
