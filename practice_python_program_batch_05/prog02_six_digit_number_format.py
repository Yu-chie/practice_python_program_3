#Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Example:
#Input: 143
#Output: 000143

#Ask User for input number
number = input("Enter a number: ")

#Format number to siz digits
formatted_number = number.zfill(6)

#Print number
print(formatted_number)