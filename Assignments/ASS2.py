def TwoCharUpward(char,n):
    for i in range(0,n,2):
        print( ((n-i)//2)*" ",char*i, ((n-i)//2)*" " )
    return

def TwoCharDownward(char,n):
    for i in range(n,0,-2):
        print( ((n-i)//2)*" ",char*i, ((n-i)//2)*" " )
    return


char = input("Enter a Character: ")
n = int(input("Enter a Incremental series limit: "))
m = int(input("Enter a decremental series limit: "))

TwoCharUpward(char,n)
TwoCharDownward(char,m)
