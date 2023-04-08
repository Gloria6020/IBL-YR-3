#prompt user for a text
text=input("Enter the string in camelCase: ")

for letter in text:
    
    if letter.isupper():
        print("_" + letter.lower(), end="")
    
    else:
        print(letter, end="")

print()