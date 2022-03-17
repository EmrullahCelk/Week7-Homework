# Write a program that detects the ID number hidden in a text. 
# We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

# Input : AABZA1111AEGTV5YH678MK4FM53B6
# Output : MK4FM53B6

# Input : AEGTV5VZ4PF94B6YH678
# Output : VZ4PF94B6

# x = int(input("Enter a number: "))
# y = int(input("Enter a second Number: "))


import re


with open("Week_7(HomeWork_1).txt", "w") as file:
    text = file.write("AABZA1111AEGTV5YH678MK4FM53B6")
    search = '["A-Za-z"]{2}[0-9]{1}["A-Za-z"]{2}[0-9]{2}["A-Za-z"]{1}[0-9]{1}' # To find the password Id number in the text
    IdNumber = re.findall(search, text)    
    print(IdNumber)





