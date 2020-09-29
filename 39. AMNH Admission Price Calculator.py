#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu
#A template for a program that computes American Museum of Natural History admission fees.
#Modified by:  Sanjidah Abdullah 

def computePrice(ageGroup, ticketType):
     """
     Takes as two parameters: the age group and the ticket type.
     Returns the AMNH admission price, as follows:

     If the ticket type is is "admission" and the age group is "adult", the price is $23.
     If the ticket type is is "admission" and the age group is  "child", the price is $13.
     If the ticket type is is "admission" and the age group is  "senior", the price is $18.
     If the ticket type is is "+exhibitions" and the age group is "adult", the price is $33.
     If the ticket type is is "+exhibitions" and the age group is  "child", the price is $20.
     If the ticket type is is "+exhibitions" and the age group is  "senior", the price is $27.
     """
     
     price = 0
     if (ageGroup == "adult" and ticketType == "admission"):
         price = 23
     elif (ageGroup == "child" and ticketType == "admission"):
         price = 13
     elif (ageGroup == "senior" and ticketType == "admission"):
         price = 18
     elif (ageGroup == "adult" and ticketType == "+exhibitions"):
         price = 33
     elif (ageGroup == "child" and ticketType == "+exhibitions"):
         price = 20
     elif (ageGroup == "senior" and ticketType == "+exhibitions"):
         price = 27
     else:
         return(-1)
     return(price)

def main():
     a = input('Enter the age group (child, adult, senior): ')
     t = input('Enter the ticket type (admission / +exhibitions): ').lower()
     price = computePrice(a,t)
     print('The price of your ticket is', price)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
