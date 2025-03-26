#Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.
#Example:
#Input: jUAn DEla CrUZ
#Output: JuaN deLA cRuz

#Ask User for name
full_name = input("Enter your name: ")

#Reverse name casing
reverse_case_name = full_name.swapcase()

#print name
print(reverse_case_name)