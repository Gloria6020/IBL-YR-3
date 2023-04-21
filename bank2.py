
"""
    The function takes user input for a greeting and returns a value based on the first letter or word
    of the greeting.
    """
def main():
    greeting = input("Enter a greeting: ")
    result = value(greeting)
    print(f"The value of your greeting is: {result}")



def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
