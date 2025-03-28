#Prog04. isupper() check if all characters of the string is on upper case.
#Create a program that do the same functionality without using isupper() function.

#Ask User for text
text = input("Enter a Text; ")

#Create a loop to iterate through each character
for char in text:
    if "a" <= char <= "z":      #If lowercase is found
        is_upper = False
        break

#Print the result
print(is_upper)