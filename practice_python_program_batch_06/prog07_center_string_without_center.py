#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. 
#Create a program that do the same functionality without using center() function.

#Ask user to enter a text and length to center
text = input("Enter a Text: ")
center_length = int(input("Enter length: "))

#Calculate spaces and center text
if len(text) < center_length:
    total_spaces = center_length - len(text)
    left_padding = total_spaces // 2
    right_padding = total_spaces - left_padding
    text = " " * left_padding + text + " " * right_padding

#Print centered string