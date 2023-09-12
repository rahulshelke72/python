def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two input numbers.
    """
    return a + b

def main():
    """
    This is the main function that demonstrates the use of docstrings.
    """
    num1 = 10
    num2 = 5
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}.")

if __name__ == "__main__":
    main()
