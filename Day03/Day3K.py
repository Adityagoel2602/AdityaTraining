largest_no=int(input('Enter largest number of series:'))
for i in range(0,largest_no+1,1):
    print(i,end=',')


largest_no=int(input('\nEnter largest number of series:'))
for i in range(largest_no,-1,-1):
    print(i,end=',')


largest_no=int(input('\nEnter largest number of series:'))
increment=int(input("Enter increment number of series:"))
for i in range(0,largest_no+1,increment):
    print(i,end=',')
