
# Name: Sanjidah Abdullah
# Session: Morning - In Class Assignment 3

import math

#1. Perfect Number
try:
    num = int(input(" 1) Enter a value to determine whether it's a perfect number: "))
    if num < 0:
        print("Invalid input. Enter positive integer only.")
    else:
        total = 0
        for i in range(1, num):
            if(num % i == 0):
                total = total + i
        if (total == num):
            print("This is a perfect number.")
        else:
            print("This is not a perfect number.")
except ValueError:
    print("Invalid input. Enter positive integer only.")

print("\n")

#2. Positive integer divisors of a user-entered number.
moreData = "n"
while moreData[0] == "n":
    try:
        n = int(input("2) Enter a positive integer: "))
        if n < 0:
            print("Invalid input. Enter positive integers only.")
        else:
            print("The divisors of",n,"are:")
            for i in range(1,n+1):
                if(n%i==0):
                    print(i)
    except:
        print("Invalid input. Enter positive integer only.")

    moreData = input("Do you want to quit (yes or no)? ")

print("\n")

#3. Triangle
moreCoordinates = "n"
while moreCoordinates[0] == "n":
    try:
        x1 = float(input("3) Enter x coordinate of point A: "))
        y1 = float(input("Enter y coordinate of point A: "))
        x2 = float(input("Enter x coordinate of point B: "))
        y2 = float(input("Enter y coordinate of point B: "))
        x3 = float(input("Enter x coordinate of point C: "))
        y3 = float(input("Enter y coordinate of point C: "))

        diff1 = float(y2-y3)
        diff2 = float(y3-y1)
        diff3 = float(y1-y2)

        area = 0.5 * (x1 * (diff1) + x2 * (diff2) + x3 * (diff3))

        if abs(area) == 0:
            print("These points do not make a triangle.")
        else:
            print("These points make a triangle.")

    except:
        print("Invalid input. Enter a valid number for the coordinate.")

    moreCoordinates = input("Do you want to quit (yes or no)? ")

print("\n")

#4. Prime numbers
moreData = "n"
while moreData[0] == "n":
    try:
        int1 = int(input("\n4) Enter the lower bound integer: "))
        int2 = int(input("Enter the upper bound integer: "))
        if int1 >= int2:
            print("Lower bound has to be less than or equal to upper bound.")
        for i in range(int1, int2 + 1):
           if i > 1:
               for n in range(2, i):
                   if (i % n) == 0:
                       break
               else:
                   print(i)
    except:
        print("Invalid input. Enter integers only.")

    moreData = input("Do you want to quit (yes or no)? ")

print("\n")

#5. Combination
moreData = "y"
while moreData[0] == "y":
    try:
        x = int(input("\n5) Enter the number of people: "))
        y = int(input("Enter a sample number within the total number of people: "))
        if y > x:
            print("The number of people must be greater than the sample number.")
        else:
            combination = math.factorial(x) / (math.factorial(y) * (math.factorial(x - y)))
            print("Given",x,"people,",y,"of them can be seated in",str(combination),"ways.")
    except:
        print("Invalid input. Enter positive integers only.")

    moreData = input("Do you have more people to seat (yes or no)? ")

print("\n")
