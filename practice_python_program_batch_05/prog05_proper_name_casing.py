#Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: Juan Dela Cruz

#Ask User for name
full_name = input("Enter your name: ")

#Correct name casing
proper_case_name = full_name.title()

#Print name
print(proper_case_name)