#Demonstrating regex
#matching ansd searching
import re

def main():
    print(re.match(r"^[a-zA-Z]+$", "abc"))
    print(re.search(r"^[a-zA-Z]+$", "abc"))

if __name__ == "__main__":
    main()
    print("Done")

import re
text = "Hello, am george"

# Match first word
match = re.search(r"\b\w+\b", text)

if match:
    print(match.group())

matches = re.findall(r"\d+", text)
print(matches)

# Matching numbers
import re

def match_numbers(string):
    numbers = re.findall(r'\d+', string)
    return numbers

# Example usage
sentence = "I have 5 apples and 10 oranges."
numbers = match_numbers(sentence)
print("Numbers found:", numbers)

# Validating email format or email password

import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False

    # Example usage
    email1 = "edwardkirumira87@gmail.com"
    email2 = "edwardkirumira.com"

    print(validate_email(email1))
    print(validate_email(email2))

# Generators and iterators
# Factorial of a number
def factorial(n):
    if n == 0:
        yield 1
    else:
        yield n * factorial(n - 1)

# Generate a function that gives the square of numbers 1 to 10
def generate_squares():
    for num in range(1, 11):
        yield num ** 2

# Example usage
squares = generate_squares()
for square in squares:
    print(square)

# Decorators in Python
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Before the function is called.")
        result = original_function(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper_function

@decorator_function
def greet(name):
    print(f"Hello, {name}!")

# Example usage
greet("John")

# Decorators
def my_decorator(func):
    def inner():
        print("hello world")
        func()
        return inner
    return inner

@my_decorator
def outer_decorator():
    print("grgrgrgrgr")

outer_decorator()
