#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter.
#Create a program that do the same functionality without using zfill() function.

#Ask User for Number and length
num = input("Enter a number: ")
length = int(input("Enter total length: "))

#Calculate zeros needed 
zeros_needed = max(0, length - len(num))

#Add zeros
zero_fill = "0" * zeros_needed + num

#Print result
print(zero_fill)