# This code is creating an infinite loop that prompts the user to enter a value for `x`. If the value
# entered is less than 0, the loop continues and prompts the user again. If the value entered is
# greater than or equal to 0, the loop breaks and the program continues.
"""while True:
    x= int(input("Enter the value of x"))
    if x >0:
        continue
    else:
        break"""
        
        
        
        
        
        
        
def main():
   
     number = get_number()
     helloworld(number)     
        
def get_number():
    while True:
        x = int(input("enter the value of x"))
        if x > 0:
            break
    return x 
    
def helloworld(x):
    for _ in range(x):
        print("Hello World")
        
        
main()

    