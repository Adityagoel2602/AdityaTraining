def printinfo(arg1, *vartuple):
    print("Output is:",arg1)
    print("Contents of variable length tuple is:",end=' ')
    for var_temp in vartuple:
        print(var_temp,end=' ')
    print()
    return
if __name__=='__main__':
    printinfo(10)
    printinfo(70,60,50)
    printinfo(70,60,'tea','samosa','chips','cake',50)
