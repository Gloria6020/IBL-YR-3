
def main():
    """
    The function takes an input value for x and determines if it is even or odd using the mod function.
    """
    x = int(input("what is the value of x?"))
    if mod(x):
        print("Even")
    else:
        print("Odd")
    
    
def mod(n):
    """
    The function checks if a given number is even or odd.
    
    :param n: an integer that we want to check if it is even or odd
    :return: The function `mod(n)` returns a boolean value `True` if the input `n` is even (i.e.,
    divisible by 2) and `False` otherwise.
    """
    if n % 2 == 0:
        return True
    else:
        return False
    
    
#return True if n % 2 == 0 else False   #combining the whole of it
#return n % 2 == 0
    
main()