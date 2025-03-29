#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. 
#Create a program that do the same functionality without using capitalize() function.

#Ask User for text
text = input("Enter a text: ")

#Capitalize first letter and convert remaining to lowercase
if text:
    first_letter = text[0]
    if "a" <= first_letter <= "z":
        first_letter = chr(ord(first_letter) - 32)          #Convert 1st letter to ascii_uppercase
        
    rest_of_text = ""
    for char in text[1:]:
        if "A" <= char <= "Z":
            rest_of_text += chr(ord(char) + 32) 
        else:
            rest_of_text += char

    #Print capitalized text
    print(first_letter + rest_of_text)