def checkeven(num1):
    if num1%2==0:
        print(num1, "is even")
    return None

def checkodd(num1):
    if num1%2==1:
        print(num1, "is odd")
    return None

num=int(input("Enter a no:"))
checkeven(num)
checkodd(num)
