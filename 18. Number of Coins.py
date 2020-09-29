#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

cents = int(input("Enter the number of cents: "))
quarters = cents // 25
print("Quarters:", quarters)
rem = cents % 25
dimes = rem // 10
print("Dimes:", dimes)
rem = rem % 10
nickels = rem // 5
print("Nickels:", nickels)
cents = rem % 5
print("Cents:", cents)
