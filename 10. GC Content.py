#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

insulin = input("Enter a DNA string: ")

#Compute the length
length = len(insulin)
print("Length is", length)

#Compute the GC-content:
numC = insulin.count('C')
numG = insulin.count('G')
gc = (numC + numG) / length
print("GC-content is", gc)

#Compute the position of first G:
positionG = insulin.find('G')
print("First G found at position", positionG)

#Compute the position of first C:
positionC = insulin.find('C')
print("First C found at position", positionC)

