#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

user = input("Enter a word: ")
codedWord = ""
for i in user:
    offset = ord(i) - ord('a') + 16
    wrap = offset % 26
    newChar = chr(ord('a') + wrap) 
    codedWord = codedWord + newChar
print("Your word in code is:", codedWord)

