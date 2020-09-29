#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import matplotlib.pyplot as plt
import pandas as pd

#Open the CSV file and store in pop
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough = input("Enter borough: ")

print("Minimum population: ", pop[borough].min())
print("Maximum population: ", pop[borough].max())
print("Average population: ", pop[borough].mean())
print("Standard deviation: ", pop[borough].std())

plt.show()
