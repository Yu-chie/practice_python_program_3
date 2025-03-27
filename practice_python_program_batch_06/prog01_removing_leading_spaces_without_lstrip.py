#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

#Ask the user to input a string with leading spaces.
text = input("Enter a text with leading spaces: ")

#Find index of first non-space characters
index = 0
while index < len(text) and text[index] == " ":
    index += 1

#Extract and print clean string()
cleaned_text = text[index:]
print(cleaned_text)
