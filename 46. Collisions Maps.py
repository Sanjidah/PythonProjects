#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

import folium
import pandas as pd

inFile = input('Enter CSV file name: ')
outputFile = input('Enter output file: ')

#Read in the CSV file into a dataframe:
fileName = pd.read_csv(inFile)

print(fileName["TIME"])

#Set up a new map object, centered at Hunter College,
#zoomed in enough to see city outline.
map1 = folium.Map(location=[40.768731, -73.964915],
                  tiles="Cartodb Positron",
                  zoom_start = 10)

for index,row in fileName.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["TIME"]
    #Add a marker for our randomly chosen landmark to the map.
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(map1)

map1.save(outfile = outputFile)
