# This code is taking user input for their favorite color and storing it in the variable `user_input`.
# Then it is printing two strings that include the user's input, one in all uppercase letters and one
# in all lowercase letters.
user_input = input("what is your favourite colour?")
print("my  favourite colour is",user_input.upper())
print("my favourite colour is",user_input.lower())

#another method of the above
# This code is taking user input for their favorite color and storing it in the variable `color`. Then
# it is printing a string that includes the user's input using string formatting with the `.format()`
# method. The `.lower()` method is used to convert the user's input to lowercase.
color=input("Which is your favorite color: ")
print("My favourite color is: {}" .format(color).lower())


