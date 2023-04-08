


# This code prompts the user to enter an arithmetic expression consistingel of two numbers and an
# operator separated by spaces. It then splits the input into three variables, converts the first and
# third variables to floats, performs the arithmetic operation based on the operator, and prints the
# result.
arithmetic = input("Enter an arithmetic expression: ")

#one has to enter a value followed by space,
#then the arguement followed by space then the last value.
x, y, z = arithmetic.split()

x1=float(x)

z1=float(z)

#conditions

if y == ("+"):
    answer=x1 + z1

elif y == ("-"):
    answer=x1-z1

elif y==("*"):
    answer=x1*z1

else: 
    answer=x1/z1

print(answer)







"""arithmetic = input("Enter an arithmetic expression: ")

#one hace to enter a value followed by space,
#then the arguement followed by space then the last value.
x, y, z = arithmetic.split()

x1=float(x)

z1=float(z)

#conditions

if y == ("+"):
    answer=x1 + z1

if y == ("-"):
    answer=x1-z1

if y==("*"):
    answer=x1*z1

if y== ("/"):
    answer=x1/z1

print(answer)"""
