def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result of division:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
    except TypeError:
        print("Error: Invalid data type for division!")
    except Exception as e:
        print("An unexpected error occurred:", e)
    else:
        print("Division operation successful!")
    finally:
        print("Division operation completed.")

# Example usage
try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    divide_numbers(num1, num2)
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")
