#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter.
#Create a program that do the same functionality without using ljust() function.

#Ask user for text and total length to justify
text = input("Enter a Text: ")
justify_length = int(input("Enter length: "))

#Calculate and append number of spaces to reach the total length.
if len(text) < justify_length:
    text += " " * (justify_length - len(text))

#Print the result