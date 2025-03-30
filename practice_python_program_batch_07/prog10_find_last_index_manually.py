#Prog10. rindex() return the first location of the function parameter in the string starting from the last character.
#Create a program that do the same functionality without using rindex() function.

#Ask User for text and substring to find
text = input("Enter a text: ")
substring = input("Enter substring to find: ")

#Find index manually from the right
index = -1
for i in range(len(text) - len(substring), -1, -1):
    if text[i:i+len(substring)] == substring:
        index = i
        break

#Print result
print(index)