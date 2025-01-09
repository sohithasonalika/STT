"""
This module demonstrates basic Python functions to test pylint compliance.
"""
def greet(name):
    """
    Returns a greeting message for the given name.

    Args:
        name (str): The name of the person to greet.

    Raises:
        ValueError: If the name is empty.

    Returns:
        str: A greeting message.
    """
    if not name:
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"

def calculate_sum(a, b):
    """
    Calculates the sum of two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def print_message():
    """
    Prints a sample message to demonstrate Python functionality.
    """
    print("This is a sample Python file to test pylint.")

if __name__ == "__main__":
    print(greet("Alice"))
    print(calculate_sum(10, 20))
    print_message()
