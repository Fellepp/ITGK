import random

parties = ['TeaParty', 'CoffeeParty', 'MilkParty', 'HouseParty', 'BeachParty']


def electionPrint(election):
    for valgdistrikt in election:
        print(valgdistrikt)


# a)
def initElection(parties):
    valgdistrikt = 92
    return [[random.randint(1000, 30000) for x in range(0, len(parties))] for y in range(0, valgdistrikt)]


election = initElection(parties)


# b)
def updateElection(election, nr, votes):
    for i in range(0, len(votes)):
        election[nr][i] += votes[i]
    return election


election = updateElection(election, 34, [123, 3321, 3342, 23, 1])
electionPrint(election)


# c)
def printLeadP(election, parties):
    leadParty = 0
    leader = ""
    for i in range(0, len(parties)):
        votes = 0
        for j in range(0, len(election)):
            votes += election[j][i]
        if votes > leadParty:
            leadParty = votes
            leader = parties[i]
    print(leader, "is leading the election with", leadParty, "votes")


printLeadP(election, parties)


# d)
def printResults(election, parties):
    res = [0 for x in range(0, len(parties) + 2)]
    for i in range(0, len(election)):
        if sum(election[i]) == 0:
            res[-1] += 1
        else:
            lead = 0
            for j in range(0, len(parties)):
                if election[i][j] > lead:
                    lead = election[i][j]
                    leadParty = j
            if lead in election[i][0:leadParty] or lead in election[i][leadParty+1:]:
                res[-2] += 1
            else:
                res[leadParty] += 1
    parties += ["Undecided (tied)", "Undecided (no votes)"]
    for i in range(0, len(res)):
        word = "delegate"
        if res[i] != 1:
            word += "s"
        print((parties[i] + ":").ljust(25) + str(res[i]).rjust(3) + " " + word)


printResults(election, parties)
