# Write a program that list according to email addresses without email domains in a text.

# Example:
# Input:
# The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. 
# Then New Yorker article on wind farms...

# Output :
# franky
# sinatra123



import re
with open('HomeWork_3.txt', 'r', encoding='utf-8') as file:
    text = file.read()
search = r'\S+@\S+'
result = re.findall(search, text)

for i in result:    
    print(i.split('@')[0])