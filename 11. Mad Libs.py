#Sanjidah Abdullah
#sabdull002@citymail.cuny.edu

template = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."
noun = input("Enter a noun: ")
template = template.replace("NOUN", noun)

verb1 = input("Enter a verb: ")
template = template.replace("VERB1", verb1)

verb2 = input("Enter another verb: ")
template = template.replace("VERB2", verb2)

print("New sentence: ", template)

