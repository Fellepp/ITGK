#a)
def add_data(user):
    userData = user.split(" ")
    return userData

#b)
def get_person(given_name, lst):
    matchingList = []
    for i in range(0, len(lst)):
        if given_name == lst[i][0]:
            matchingList.append(lst[i])
    return matchingList

def main():
    print('Hello, welcome to Facebook. Add a new user by writing "given_name surname age gender relationship_status".')
    done = ""
    facebook = []
    while(done!="done"):
        user = input("Add a new user: ")
        facebook.append(add_data(user))
        done = user
    print("OK")
    done= ""
    while(done!="done"):
        given_name = input("Search for a user: ")
        print(get_person(given_name, facebook))
        done = given_name
    print("OK")

main()