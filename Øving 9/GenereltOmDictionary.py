#a, b)
my_family = {}

def add_family_member(role, name):
    if role not in my_family.keys():
        my_family[role] = [name]
    else:
        my_family[role].append(name)
    return my_family

def print_dictionary(dict):
    for keys, values in dict.items():
        print(keys)
        print(values)

def main():
    notDone = True
    while(notDone):
        family = input("Skriv inn rolle og navn på formen 'rolle navn' ")
        lst = family.split(" ")
        role = lst[0]
        name = lst[1]
        add_family_member(role, name)
        print_dictionary(my_family)
        done = input("Legge til flere familiemedlemmer? (j/n) ")
        if (done == "n"):
            notDone = False

main()
