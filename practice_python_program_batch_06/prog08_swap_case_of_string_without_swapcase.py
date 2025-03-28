#Prog08. swapcase() reverse the casing of each of the character of the string. 
#Create a program that do the same functionality without using swapcase() function.

#Ask User to enter text
text = input("Enter a string: ")

#Loop through each character and swap its case
case_swapped_text = ""

for char in text:
    if "a" <= char <= "z":
        case_swapped_text += chr(ord(char) - 32)
    elif "A" <= char <= "Z":
        case_swapped_text += chr(ord(char) + 32)
    else:
        case_swapped_text += char

#Print swapped case text