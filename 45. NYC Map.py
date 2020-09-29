#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

#Import the folium package for making maps
import folium

#Create a map, centered (40.75, -74.125):
mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

#Add marker for Hunter College
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

#Save the map:
mapCUNY.save(outfile="nycMap.html")
