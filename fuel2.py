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
