def printNymbers(Lrange, Urange):
    # base case
    if Lrange > Urange:
        return 
    else:
        print(Lrange)
        printNymbers(Lrange + 1, Urange)
printNymbers(1, 10)
# just by chnaging a place of node we can print the numbers in reverse order
def printNymbersd(Lrange, Urange):
    # base case
    if Lrange > Urange:
        return 
    else:
        printNymbersd(Lrange + 1, Urange)
        print(Lrange)
printNymbersd(1, 10)