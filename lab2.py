# Name: Sanjidah Abdullah
# Session: Morning - In Class Assignment 2

import math

#A: Minutes to Milliseconds
def minutes_to_milliseconds(minutes):
    minutes = int(minutes)
    millis = (minutes * 60000)
    return millis

minutes = input("A) Enter time in minutes: ")
conversion = minutes_to_milliseconds(minutes)
print("Equivalent to", conversion, "milliseconds")
#Example Results: Enter time in minutes: 1
#Equivalent to 60000 milliseconds

#B: Average of Two Exam Scores
def average(exam1,exam2):
    exam1 = int(exam1)
    exam2 = int(exam2)
    grade = ((exam1+exam2)/2)
    return (grade)

exam1 = input("B) Enter the first exam score: ")
exam2 = input(" Enter the second exam score: ")
calculation = average(exam1,exam2)
print("Average is ", calculation)
#Example Results: Enter the first exam score: 2
#Enter the second exam score: 3
#Average is  2.5

#C Roots of a Quadratic Equation
def roots(a,b,c):
    r = (b**2)-(4*a*c)
    x1 = (((-b) + math.sqrt(r))/(2*a))
    x2 = (((-b) - math.sqrt(r))/(2*a))
    return (x1,x2)

a = float(input("C) Please enter a: "))
b = float(input(" Please enter b: "))
c = float(input(" Please enter c: "))
quadratic_roots = roots(a,b,c)
print("Roots are ", quadratic_roots)
#Example Results:  Please enter a: 1
#Please enter b: 2
#Please enter c: 1
#Roots are  (-1.0, -1.0)


#D Temperature Conversion
def Kelv_to_Reau(kelvin):
    kelvin = float(kelvin)
    reaumer = (kelvin -273.15) * (4/5)
    return reaumer

def Reau_to_celsius(reau):
    reaumer = Kelv_to_Reau(reau)
    celsius = reaumer*(5/4)
    return celsius

temp1 = input("D) Enter kelvin value: ")
conversion1 = Kelv_to_Reau(temp1)
print(temp1,"kelvins is equivalent to", conversion1 , "reaumers")
conversion2 = Reau_to_celsius(temp1)
print(conversion1," reaumers is equivalent to", conversion2, "celsius")
#Example Results: 2 kelvins is equivalent to -216.92 reaumers
# -216.92  reaumers is equivalent to -271.15 celsius


#E Marbles in Cube
def volumeSphere(n):
    radius = n/4
    volSp = (radius ** 3) * math.pi * (4/3)
    return  volSp

def volumeCube(n):
    volC = n**3
    return volC

def marbles(n):
    return math.floor(volumeCube(n) / volumeSphere(n))

n = input("Enter value of n: ")
n = float(n)
print(marbles(n),"marbles can fit in the cube")
#Example Results: Enter value of n: 10
# 15 marbles can fit in the cube

#F Pattern
def pat1():
    print("^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^ _ ^ _ ^^")

def pat2():
    print("i        i        i        i        i")

def pattern2():
    pat2()
    pat2()
    pat2()
    pat2()

def line1():
    pat1()
    pattern2()
    pat1()
    pattern2()
    pat1()
    pattern2()
    pat1()
    pattern2()
    pat1()

def printPat():
    line1()

printPat()
