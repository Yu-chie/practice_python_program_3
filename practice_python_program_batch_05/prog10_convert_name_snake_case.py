#Prog10: Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
#Example:
#Input: jUAn DEla CrUZ
#Output: juan_dela_cruz

#Ask User for name
full_name = input("Enter your name: ")

#Convert name to snake case
snake_case_name = full_name.lower().replace(" ", "_")

#print name
print(snake_case_name)