#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu
import matplotlib.pyplot as plt
import numpy as np

num = int(input("Enter the size: "))
file = str(input("Enter output file: "))

img = np.ones( (num,num,3) )
img[:,::2,:2] = 0      #All rows, all columns but step 2, blue channel 

plt.imsave(file, img)
