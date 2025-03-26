#Prog07: Create a program that ask the user to input a complete statement. Print the number of words in the input.
#Example:
#Input: We will weather the weather whatever the weather whether we like it or not
#Output: 14

#Ask User for a statement
statement = input("Enter a statement: ")

#Count number of words
word_count = len(statement.split())

#Print number of words
print(word_count)