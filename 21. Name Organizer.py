#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

people = input("Please enter your list of names: ")
namesList = people.split(',')
print(namesList)

for names in namesList:
    firstNames = names.split()
    print(firstNames[1][0] + ". " + firstNames[0])
