#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#Ask User for text and a prefix to remove
text = input("Enter a text: ")
prefix = input("Enter prefix to remove: ")

#Check if text starts with the prefix
if text [:len(prefix)] == prefix:
    text = text[len(prefix): ]          #Remove prefix

#Print modified text