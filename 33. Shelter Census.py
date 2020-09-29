#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import pandas as pd
import matplotlib.pyplot as plt

inputFile = input("Enter name of input file: ")
outputFile = input("Enter name of output file: ")

homeless = pd.read_csv(inputFile)
homeless['Fraction Single'] = homeless['Total Single Adults in Shelter']/homeless['Total Individuals in Shelter']

homeless.plot(x = "Date of Census", y = "Fraction Single")

fig = plt.gcf()
fig.savefig(outputFile)
plt.show()



