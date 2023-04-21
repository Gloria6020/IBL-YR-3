import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Use regex to match "um" as a word, case-insensitively
    pattern = r"\bum\b"
    um_count = len(re.findall(pattern, s, re.IGNORECASE))
    return um_count


if __name__ == "__main__":
    main()
