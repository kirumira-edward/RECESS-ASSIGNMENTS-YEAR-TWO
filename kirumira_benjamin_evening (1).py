#error handling
import xdrlib
try:
    print(xdrlib)
except NameError:
    print("Error: Variable x is not defined.")

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
try:
    num1 = 10
    num2 = "20"
    result = num1 + num2
except TypeError:
    print("Error: Unsupported operand type(s) for +.")

# ValueError: invalid literal for int() with base 10
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid literal for int().")

# ZeroDivisionError: division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero.")

# FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent.txt'
try:
    with open("nonexistent.txt", "r") as file:
        contents = file.read()
except FileNotFoundError:
    print("Error: File not found.")

# IndexError: list index out of range
try:
    my_list = [1, 2, 3]
    print(my_list[4])
except IndexError:
    print("Error: List index out of range.")

# KeyError: 'key3'
try:
    my_dict = {"key1": 1, "key2": 2}
    print(my_dict["key3"])
except KeyError:
    print("Error: Key not found in dictionary.")

# AssertionError: Assertion failed
try:
    assert 2 + 2 == 5, "Assertion failed."
except AssertionError as e:
    print(f"Error: {str(e)}")


# KeyboardInterrupt: User interrupt
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Error: User interrupted the program.")






#file handling
import os

# File path
file_path = "path/to/file.txt"  # Replace with the actual file path

# Open file in write mode and write content
with open(file_path, "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.")

# Open file in read mode and read content
with open(file_path, "r") as file:
    contents = file.read()
    print("File Contents:")
    print(contents)

# Open file in append mode and add content
with open(file_path, "a") as file:
    file.write("\nAppending new content.")

# Open file in read mode again and read updated content
with open(file_path, "r") as file:
    contents = file.read()
    print("\nUpdated File Contents:")
    print(contents)

# Open file in write mode and overwrite content
with open(file_path, "w") as file:
    file.write("This is a new content.")

# Open file in read mode and read updated content
with open(file_path, "r") as file:
    contents = file.read()
    print("\nNew File Contents:")
    print(contents)

# Delete the file
os.remove(file_path)
print("\nFile Deleted.")
