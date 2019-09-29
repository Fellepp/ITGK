def find_rate(filename, check_rate, acc):
    rates = ""
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                lst = line.split(" ")
                rate = float(lst[1])
                if round(rate, acc) == round(check_rate, acc):
                    print(line)
    except IOError:
        print("Feil: Finner ikke fila eller har ikke lesetilgang!")
    except Exception:
        print("Feil: Det er noe feil med argumentene!")
find_rate("USD_NOK.txt", 6.2, 2)
