#Prog05. endswith() check if the string end part matches the function parameter. 
#Create a program that do the same functionality without using endswith() function.

#Ask User for text and suffix to check
text = input("Enter a text: ")
suffix = input("Enter a suffix to check: ")

#Get the length of the suffix
suffix_length = len(suffix)
extracted_string = text[-(suffix_length):]

#Compare last characters of text with suffix
if suffix == extracted_string:
    print(True)         #Print Result
else:
    print(False)         #Print Result