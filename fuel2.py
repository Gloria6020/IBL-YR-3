"""
    The function takes a fraction input in X/Y format, converts it to a percentage, and returns a gauge
    reading based on the percentage.
    
    :param fraction: The fraction of the fuel tank that is filled, entered by the user in X/Y format
    (where X and Y are integers)
    :return: The program prompts the user to enter a fraction in X/Y format representing the percentage
    of a fuel tank that is filled. It then converts the fraction to a percentage, rounds it to the
    nearest whole number, and passes it to the `gauge` function. The `gauge` function returns a string
    representing the fuel gauge level based on the percentage. If the percentage is less than or equal
    to
    """
    
    
def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        percentage = round((x / y) * 100)
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100, inclusive.")
        return percentage
    except ValueError:
        raise ValueError("Input must be in X/Y format with integers for X and Y.") from None
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot be 0.") from None


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    fraction = input("Enter the fraction of the fuel tank that is filled (in X/Y format): ")
    try:
        percentage = convert(fraction)
        print(f"The tank is {gauge(percentage)}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
