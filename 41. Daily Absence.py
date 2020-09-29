#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

inputFile = input("Enter name of input file: ")
outputFile = input("Enter name of output file: ")

school = pd.read_csv(inputFile)
school["Date"] = pd.to_datetime(school["Date"].apply(str))	

school['% Absent'] = (school['Absent']/school['Enrolled'] * 100)

school.plot(x = "Date", y = "% Absent")

fig = plt.gcf()
fig.savefig(outputFile)
plt.show()
