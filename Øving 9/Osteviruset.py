cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A234-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}

#a)
for keys, values in cheeses.items():
    if 'port salut' in keys:
        print(values)

#b)
infected_cheeses = []
potentially_infected = ["B15", "A234", "C31", "A235"]

for keys in cheeses:
    for values in cheeses[keys]:
        for j in potentially_infected:
            if j in values and keys not in infected_cheeses:
                infected_cheeses.append(keys)

print("Potentialy infected cheeses: ", infected_cheeses)

#Søke på key og printe ut value
"""cheese = input("Skriv inn en ost ")
for keys in cheeses:
    if cheese in cheeses:
        print(cheeses[cheese])
        break
    else:
        print("Fant ikke ost")"""

#c)
print(cheeses.items())
for key, value in cheeses.items():
    if key not in infected_cheeses:
        for i in value:
            print(i, ",", key)