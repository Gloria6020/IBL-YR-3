# This code prompts the user to input an answer to the question "What is Answer to the Great Question
# of Life, the Universe and Everything?" and then checks if the answer is equal to "42", "forty two",
# or "forty-two". If the answer matches any of these options, the code will print "Yes". Otherwise, it
# will print "No".
answ = input("What is Answer to the Great Question of Life, the Universe and Everything? ")

if answ == "42" or answ == "forty two" or answ == "forty-two":
    print("Yes")
else:
    print("No")
    answ = input("What is Answer to the Great Question of Life, the Universe and Everything? ")

if answ == "42":
    print("Yes")
elif answ == "forty-two":
    print("Yes")
elif answ == "forty two":
    print("Yes")
else:
    print("No")
    