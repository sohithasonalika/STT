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
    return a + b

def print_message():
    print("This is a sample Python file to test pylint.")

if __name__ == "__main__":
    print(greet("Alice"))
    print(calculate_sum(10, 20))
    print_message()
