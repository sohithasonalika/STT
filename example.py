def greet(name):
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
