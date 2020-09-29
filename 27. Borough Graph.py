#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough = input("Enter borough name: ")
file = input("Enter output file name: ")

#Compute the fraction of the population in the given borough
#and save as new column:
pop['Fraction'] = pop[borough]/pop['Total']

#Create a plot of year versus fraction of pop. in given borough (with labels):
pop.plot(x = 'Year', y = 'Fraction')

#Save to given file:
fig = plt.gcf()
fig.savefig(file)

plt.show()
