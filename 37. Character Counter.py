#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

code = str(input("Please enter a codeword: "))
upper = 0
lower = 0
num = 0
special = 0

for i in code:
    if (ord(i) >= 97 and ord(i) <= 122):
        lower = lower + 1
    elif (ord(i) >= 65 and ord(i) <= 90):
        upper = upper + 1
    elif (ord(i) >= 48 and ord(i) <= 57):
        num = num + 1
    else:
        special = special + 1
    
print("Your codeword contains", upper, "uppercase letters,",
      lower, "lowercase letters,", num, "numbers, and", special,
      "special characters.")

