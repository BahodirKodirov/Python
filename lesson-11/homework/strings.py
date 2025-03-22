Create your own virtual environment and install some python packages.
  # Create the virtual environment
python -m venv myenv

# Activate the virtual environment
source myenv/bin/activate  # For macOS/Linux
# or
myenv\Scripts\activate     # For Windows

# Install packages
pip install numpy requests

# List installed packages
pip list

# Deactivate when done
deactivate

  Create custom modules.
Create math_operations.py module. Define add, subtract, multiply and divide functions in it. (All functions accept two arguments in this task)
Create string_utils.py module. Define reverse_string and count_vowels functions in it. (All functions accept one argument in this task)

  # math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"




# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count



# main.py

# Importing functions from the custom modules
from math_operations import add, subtract, multiply, divide
from string_utils import reverse_string, count_vowels

# Using math_operations functions
print("Addition:", add(5, 3))
print("Subtraction:", subtract(5, 3))
print("Multiplication:", multiply(5, 3))
print("Division:", divide(5, 3))

# Using string_utils functions
print("Reversed String:", reverse_string("hello"))
print("Vowel Count:", count_vowels("hello"))


Create custom packages.
Create geometry package.
 geometry\
     __init__.py
     circle.py
 
Define calculate_area and calculate_circumference functions in circle.py. These functions accept one argument(radius).
Create file_operations package.
 file_operations\
     __init__.py
     file_reader.py
     file_writer.py
 
Define read_file function in file_reader.py. This function accepts one argument(file_path). Define write_file function in file_writer.py. This function accepts two arguments(file_path, content).

# geometry/__init__.py

# You can also import functions here if you want to make them easier to access:
# from .circle import calculate_area, calculate_circumference

# geometry/circle.py

import math

def calculate_area(radius):
    return math.pi * radius * radius

def calculate_circumference(radius):
    return 2 * math.pi * radius

# file_operations/__init__.py

# You can also import functions here for easier access:
# from .file_reader import read_file
# from .file_writer import write_file


# file_operations/file_reader.py

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"File not found: {file_path}"
    except Exception as e:
        return str(e)


# file_operations/file_writer.py

def write_file(file_path, content):
    try:
        with open(file_path, 'w') as file:
            file.write(content)
        return f"Content successfully written to {file_path}"
    except Exception as e:
        return str(e)

""""""
your_project_folder/
│
├── geometry/
│   ├── __init__.py
│   └── circle.py
│
└── file_operations/
    ├── __init__.py
    ├── file_reader.py
    └── file_writer.py
""""""

# main.py

# Importing functions from geometry and file_operations packages
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

# Using functions from the geometry package
radius = 5
print("Area of the circle:", calculate_area(radius))
print("Circumference of the circle:", calculate_circumference(radius))

# Using functions from the file_operations package
file_path = 'sample.txt'
content = 'Hello, this is a sample file.'

# Writing to the file
print(write_file(file_path, content))

# Reading from the file
print(read_file(file_path))

