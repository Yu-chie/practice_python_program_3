#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter.
#Create a program that do the same functionality without using removesuffix() function.

#Ask User for text and suffix to remove
text = input("Enter a text: ")
suffix = input("Enter suffix to remove: ")

#Check if text ends with the suffix
if text[-len(suffix):] == suffix and len(suffix) <= len(text):
    text = text[:-len(suffix)]

#Print result