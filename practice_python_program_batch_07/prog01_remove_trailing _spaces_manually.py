#Prog01. rstrip() remove the space characters at the end of the string. 
#Create a program that do the same functionality without using rstrip() function.

#Ask User for text
text = input("Enter a text: ")

#Find the last non-space character
last_char_index = len(text) -1
while last_char_index >= 0 and text[last_char_index] == " ":
    last_char_index -= 1

#Extract string up to the last non space character
cleaned_text = text[:last_char_index +1]

#Print the cleaned text
print(cleaned_text)