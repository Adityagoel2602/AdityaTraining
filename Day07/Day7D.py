def printblue():
    print('You choose blue\n')
    return

def printred():
    print('You choose red\n')

def printorange():
    print('You choose orange\n')

def printyellow():
    print('You choose yellow\n')

def choice():
    print("0:Blue")
    print("1:Red")
    print("2:Orange")
    print("3:Yellow")
    print("4:Quit")
    return

colorselect={0:printblue, 1:printred, 2:printorange, 3:printyellow }
selection=0
while True: #(selection!=4):
    if selection==4:
        break
    choice()
    selection=int(input("select a color option:"))
    if (selection>=0)and(selection<4):
        colorselect[selection]()
