#Prog03. upper() converts all characters of the string into upper case.
#Create a program that do the same functionality without using upper() function.

#Ask User for text
text = input("Enter a text: ")

#Convert to uppercase Manually
uppercase_text = ""
for char in text:
    if "a" <= char <= "z":      # Check if lowercase   
        uppercase_text += chr(ord(char) - 32)       # Convert to uppercase
    else:
        uppercase_text += char
        
#Print uppercase text

