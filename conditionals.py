# `x=int(input("enter the value of x "))` is taking input from the user and storing it in the variable
# `x` as an integer. Similarly, `y=int(input("enter the value of y "))` is taking input from the user
# and storing it in the variable `y` as an integer.
x=int(input("enter the value of x "))
y=int(input("enter the value of y "))

# This code is comparing the values of two variables `x` and `y` using conditional statements. If `x`
# is less than `y`, it will print "x is less than y". If `x` is greater than `y`, it will print "x is
# greater than y". If `x` is equal to `y`, it will print "x is equal to y".
if x < y:
    print("x is less than y")
    
if x > y:
     print("x is greater than y")
     
if x == y:
    print("x is equal to y")
    
    
    

    
    # This code is also comparing the values of two variables `x` and `y` using conditional
    # statements. However, it is using the `elif` and `else` statements to make the code more concise.
    # If `x` is less than `y`, it will print "x is less than y". If `x` is greater than `y`, it will
    # print "x is greater than y". If `x` is equal to `y`, it will print "x is equal to y". The `else`
    # statement is used to catch any other cases that were not covered by the previous `if` and `elif`
    # statements. In this case, it is checking if `x` is equal to `y` and printing the corresponding
    # message.
    if x < y:
        print("x is less than y")
    
    elif x > y:
        print("x is greater than y")
     
    else:
        print("x is equal to y")
    