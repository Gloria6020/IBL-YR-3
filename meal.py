def main():
    """
    The function takes user input for time, converts it to decimal format, and prints out a message
    based on the time range.
    """
    answer = input("What is the time: ")

    time = convert(answer)
#conditions
    if time >= 7 and time <= 8:
        print("Breakfast time")

    if time >= 12 and time <=13:
        print("lunch time")

    if time >=18 and time <=19:
        print("dinner time")

def convert(time):

    hours, minutes = time.split(":")

    new_minute = float(minutes)/60

    return float(hours) + new_minute

# `if __name__ == "__main__":` is a conditional statement that checks if the current script is being
# run as the main program. If it is, then it calls the `main()` function. This is a common Python
# idiom that allows a script to be used both as a standalone program and as a module that can be
# imported into other programs.
if __name__ == "__main__":
    main()