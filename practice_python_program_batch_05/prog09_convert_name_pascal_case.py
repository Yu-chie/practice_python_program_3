#Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuanDelaCruz

#Ask User for name
full_name = input("Enter your name: ")

#Convert name to pascal case
pascal_case_name = full_name.title().replace(" ", "")

#Print name
print(pascal_case_name)