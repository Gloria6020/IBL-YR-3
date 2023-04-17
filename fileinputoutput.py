name = input("what is your name")

# This code is opening a file named "names.txt" in append mode ("a"), which means that any new data
# written to the file will be added to the end of the existing data. It then writes the value of the
# variable `name` followed by a newline character ("\n") to the file, and finally closes the file.
# This code is essentially adding the value of `name` to a list of names stored in the "names.txt"
# file.
"""file = open("names.txt","a")
file.write(f"{name}\n")
file.close()
"""

with open("names.txt","a") as file:
    file.write(f"{name}\n")