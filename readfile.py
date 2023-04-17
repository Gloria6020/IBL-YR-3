# This code is opening a file named "names.txt" in read mode using the `with` statement, which
# ensures that the file is properly closed after it is used. It then reads all the lines in the
# file using the `readlines()` method and stores them in a list called `lines`. It then iterates
# over each line in the `lines` list using a `for` loop and prints "Hello," followed by the
# stripped line. The `rstrip()` method is used to remove any trailing whitespace characters from
# the line.
"""with open("names.txt", "r") as file:
    lines =  file.readlines()
    
for line in lines:
    print("Hello,", line.rstrip())"""
    
    
    
# This code is opening a file named "names.txt" in read mode using the `with` statement, which ensures
# that the file is properly closed after it is used. It then iterates over each line in the file using
# a `for` loop and prints "Hello," followed by the stripped line. The `rstrip()` method is used to
# remove any trailing whitespace characters from the line.
with open("names.txt","r") as file:
    for line in file:
        print("Hello,", line.rstrip())