score = int(input("score"))

# This code is taking an input from the user as a score and then checking the score against different
# ranges to determine the grade. If the score is between 90 and 100, it will print "grade: A". If the
# score is between 80 and 90, it will print "grade: B". If the score is between 70 and 80, it will
# print "grade: C". If the score is between 60 and 70, it will print "grade: D". If the score is less
# than 60, it will print "grade: f". However, there is a mistake in the code as the last else
# statement is only associated with the last if statement, not all of them. This can be corrected by
# using elif statements instead of multiple if statements.
if score >= 90 and score <= 100:
    print("grade: A")
if score >= 80 and score <= 90:
    print("grade: B")
if score >= 70 and score <= 80:
    print("grade: C")
if score >= 60 and score <= 70:
    print("grade: D")
else:
    print("grade: f")
    
    
    
# This code is taking an input from the user as a score and then checking the score against different
# ranges to determine the grade. If the score is between 90 and 100, it will print "grade: A". If the
# score is between 80 and 90, it will print "grade: B". If the score is between 70 and 80, it will
# print "grade: C". If the score is between 60 and 70, it will print "grade: D". If the score is less
# than 60, it will print "grade: f". This code is using elif statements instead of multiple if
# statements to ensure that the else statement is associated with all the if statements.
if 90 <= score <= 100:
    print("grade: A")
elif score >= 80 and score <= 90:
    print("grade: B")
elif score >= 70 and score <= 80:
    print("grade: C")
elif score >= 60 and score <= 70:
    print("grade: D")
else:
    print("grade: f")
    
    
    
    
# This code is taking an input from the user as a score and then checking the score against different
# ranges to determine the grade. If the score is greater than or equal to 90, it will print "grade:
# A". If the score is greater than or equal to 80, it will print "grade: B". If the score is greater
# than or equal to 70, it will print "grade: C". If the score is greater than or equal to 60, it will
# print "grade: D". If the score is less than 60, it will print "grade: f". This code is using elif
# statements instead of multiple if statements to ensure that the else statement is associated with
# all the if statements.
if score >= 90:
    print("grade: A")
elif score >= 80:
    print("grade: B")
elif score >= 70:
    print("grade: C")
elif score >= 60:
    print("grade: D")
else:
    print("grade: f")      