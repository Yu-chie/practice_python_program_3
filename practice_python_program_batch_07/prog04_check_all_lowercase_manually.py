#Prog04. islower() check if all characters of the string is on lower case. 
#Create a program that do the same functionality without using islower() function.

#Ask user for Text
text = input("Enter a text: ")

#Check if letters are lowercased manually
all_lowercase = True
for char in text:
    if "A" <= char <= "Z":      #If uppercase found
        all_lowercase = False
        break

#Print result
print(all_lowercase)
