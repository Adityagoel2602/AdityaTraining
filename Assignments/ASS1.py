def printSeriesIncrease(char,n):
    for i in range(n):
        print(char*i)

    return

def printSeriesDecrease(char,n):
    for i in range(n,0,-1):
        print(char*i)
    return

char = input("Enter a Character: ")
n = int(input("Enter a Incremental series limit: "))
m = int(input("Enter a decremental series limit: "))

printSeriesIncrease(char,n)
printSeriesDecrease(char,m)
