#a)
def write_to_file(data):
    f = open("my_file.txt", "w")
    f.write(data)
    f.close

#b)
def read_from_file(filename):
    f = open(filename, "r")
    innhold = f.read()
    print(innhold)

#c)
def main():
    done = ""
    while(done != "done"):
        valg = input("Do you want to read or write? ")
        if(valg == "write"):
            q = input("What do you want to write to file? ")
            write_to_file(q)
            print(q + " was written to file")
        elif(valg == "read"):
            try:
                read_from_file("my_file.txt")
            except:
                print("There's no existing file. Please write first")
        done = valg
        
main()