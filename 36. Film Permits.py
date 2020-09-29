#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

#Import pandas for reading and analyzing CSV data:
import pandas as pd

#Name of the CSV file
csvFile = input("Enter file name: ")

#Read in the file to a dataframe
film = pd.read_csv(csvFile)

#Prints total number of permits in the file
permits = len(film)
print("There were", permits, "film permits.")

#Prints count of permits for each borough
print(film["Borough"].value_counts())

#Prints five most popular locations
print("The five most popular filming locations were")
print(film["ParkingHeld"].value_counts()[:5])
