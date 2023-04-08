user=input("enter the text:")
print("output: ", end="")
for letter in user:
    if not letter.lower() in['a','e','i','o','u']:
        print(letter, end="")
print()