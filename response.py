"""
    The function takes user input for an email address and uses a validator to determine if it is valid
    or not.
    """
from validator_collection import validators
def main():
    email = input("Enter an email address: ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()



#another way using the regex method
import re

def main():
    email_regex = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    email = input("Enter an email address: ")
    if re.match(email_regex, email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
