

# The code is creating a list of students and a list of estates, and then creating a dictionary that
# maps each student to their corresponding estate. Finally, it prints the estate of the student named
# "kevin".
#student =["kevin", "sheldon", "brian","john"]
estates =["kasarani", "exit 9", "syokimau", "kayole", "ngara"]

students ={
    "kevin":"kasarani",
    "sheldon":"exit 9",
    "brian":"syokimu",
    "john":"kayole",
    "joy":"ngara"
}

"""print(students["kevin"])"""

for student in students:
    print(student, students[student], sep="___")
