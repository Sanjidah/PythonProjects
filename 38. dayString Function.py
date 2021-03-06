#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

def dayString(dayNum):
     """
     Takes as input a number, dayNum, and
     returns the corresponding day name as a string.
     Example: dayString(1) returns "Monday".
     Assumes that input is an integer ranging from 1 to 7
     """
     
     dayString = ""
     if dayNum == 0:
         dayString = "Sunday"
     elif dayNum == 1:
         dayString = "Monday"
     elif dayNum == 2:
         dayString = "Tuesday"         
     elif dayNum == 3:
         dayString = "Wednesday"
     elif dayNum == 4:
         dayString = "Thursday"
     elif dayNum == 5:
         dayString = "Friday"
     elif dayNum == 6:
         dayString = "Saturday"
     elif dayNum == 7:
         dayString = "Sunday"
     return(dayString)



def main():
     n = int(input('Enter the number of the day: '))
     dString = dayString(n)
     print('The day is', dString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
