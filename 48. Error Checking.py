#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

num = int(input("Please enter number: "))
total = 1
sumNum = num
avg = sumNum/total

while (avg < 50):
    num = int(input("Please enter number: "))
    total = total + 1
    sumNum = sumNum + num
    avg = sumNum/total
print("The average is", avg)

#OR

total = 0
sumNum = 0
avg = 0
while (avg < 50):
    num = int(input("Please enter number: "))
    total = total + 1
    sumNum = sumNum + num
    avg = sumNum/total
print("The average is", avg)
