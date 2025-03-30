#Prog05. startswith() check if the string beginning part matches the function parameter.
#Create a program that do the same functionality without using startswith() function.

#Ask User for text and prefix
text = input("Enter a text: ")
prefix = input ("Enter prefix to check: ")

#Check if text starts with prefix
starts_with = text[:len(prefix)] == prefix if len(prefix) <= len(text) else False

#print result
print(starts_with)