#Prog09. index() return the first location of the function parameter in the string.
#Create a program that do the same functionality without using index() function.

#Ask User for text and substring to find
text = input("Enter a text: ")
substring = input("Enter substring to find: ")

#Find index manually
index = -1
for i in range(len(text)- len(substring) + 1):
    if text[i:i+len(substring)] == substring:
        index = 1
        break
    
#Print result
print(index)