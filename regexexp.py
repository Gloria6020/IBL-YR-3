import re

email = input("whats your email?") .strip()

#username, domain = email.split("@")

#if "@" in email and "." in email:
#if username and domain.endswith(".com"):
# `if re.search(r"\^.+@.+\.com$", email):` is using regular expression to check if the email entered
# by the user is valid or not. The regular expression pattern `r"\^.+@.+\.com$"` matches any string
# that starts with `^`, followed by one or more characters `.+`, followed by `@`, followed by one or
# more characters `.+`, followed by `.com`, and ends with `$`. If the email matches this pattern, it
# is considered valid.
if re.search(r"^[a-zA-Z0].+@[^@].+\.com\$", email):
    print("valid")
else:
    print("invalid")
    