#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter.
#Create a program that do the same functionality without using rjust() function.

#Ask User for text and spaces to justify
text = input("Enter a text: ")
length = int(input("Enter total width: "))


#Calculate spaces needed
spaces_needed = max(0, length - len(text))

#Create right-justified text 
right_justified = " " * spaces_needed + text

#Print result
print(right_justified)