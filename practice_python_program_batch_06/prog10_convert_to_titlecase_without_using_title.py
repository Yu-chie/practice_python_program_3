#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
#Create a program that do the same functionality without using title() function.

#Ask User for text
text = input("Enter a text: ")

#Convert each word to title case
words = text.split()
title_cased_words = []
for word in words:
    if word:
        title_word = chr(ord(word[0]) - 32) if "a" <= word[0] <= "z" else word[0]
        title_word += "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in word[1:])
        title_cased_words.append(title_word)

#Print title cased text