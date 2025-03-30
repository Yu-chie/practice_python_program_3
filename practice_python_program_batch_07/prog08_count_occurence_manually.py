#Prog08. count() return how many time the function parameter appear in the string. 
#Create a program that do the same functionality without using count() function.

#Ask user for text and substring
text = input("Enter a text: ")
substring = input("Enter substring to count: ")

#Manual count
count = 0
index = 0

while index <= len(text) - len (substring):
    if text[index:index+len(substring)] == substring:
        count += 1
    index += 1

#Print result