#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import pandas as pd

inputFile = input("Enter file name: ")
star = input("Enter the name of the star type: ")

#Read in the csv file.
starNames = pd.read_csv(inputFile)

#Group the data by Start type get max and min for given star type.
largest = starNames.groupby('Star type').get_group(star).max()
smallest = starNames.groupby('Star type').get_group(star).min()

#Print radii of the largest and smallest star for given star type.
print("The radius of the largest", star,"is", largest['Radius(R/Ro)'])
print("The radius of the smallest", star,"is", smallest['Radius(R/Ro)'])
