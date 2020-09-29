#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

#Import the packages for images and arrays:
import matplotlib.pyplot as plt #import libraries for plotting
import numpy as np #and for arrays (to hold images)
logoImg = np.ones((30,30,3)) #30x30 array with 3 sheets of 1’s

#Turn the green and blue channels of first 10 columns to 0
logoImg[:,:10,1] = 0
logoImg[:,:10,2] = 0 

#Turn the green and blue channels of last 10 columns to 0
logoImg[:,-10:,1] = 0 
logoImg[:,-10:,2] = 0 

#Turn green and blue channels of bottom 3rd of image to 0
logoImg[20:30,:,1] = 0 
logoImg[20:30,:,2] = 0 

plt.imsave("logo.png", logoImg) #Save the image to logo.png

