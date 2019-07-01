year = int(input("Enter period: "))

sum = 100

for i in range(year):
    sum += sum*0.05


compund = sum * ( 1+0.05 ** (1 * year))

print("Sum after (Simple)",year,"=",round(sum,2))
print("Sum after (Compound)",year,"=",round(compund,2))
