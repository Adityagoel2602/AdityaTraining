#minutes in a year

year=int(input("Enter year: "))

if((year%4==0)and(year%100!=0 or year%400==0)):
   print("Number of minutes(leap year):",366*24*60,"min")

else:
   print("Number of minutes(non-leap year):",365*24*60,"min")
