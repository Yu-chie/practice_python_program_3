#Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Example:
    #Input:         Juan Dela Cruz
    #Output: Juan Dela Cruz

#Ask User to input their Name
full_name = input("Enter your Full Name: ")

#Remove leading spaces
clean_fullname = full_name.lstrip()

#Print Name
print("Full name: ", clean_fullname)