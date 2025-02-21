Puzzle 1: Write to a File 
Create a file example.txt and write "Hello, World!" using w mode.
with open('example.txt', 'w') as file:
 
    file.write("Hello, World!")

print("File 'example.txt' created and written successfully.")
Puzzle 2: Append to a File 
Append "This is an appended line." to example.txt.


with open('example.txt', 'a') as file:

    file.write("\nThis is an appended line.")

print("Text appended to 'example.txt' successfully.")
Puzzle 3: Read a File 
Read and print the content of example.txt.
with open('example.txt', 'r') as file:
   
    content = file.read()


print("Content of 'example.txt':")
print(content)
Puzzle 4: Write and Read a File
Write "Python is fun!" to test.txt and read it

with open('test.txt', 'w+') as file:
    file.write("Python is fun!")
    file.seek(0)  
    content = file.read()

print("Content of 'test.txt':")
print(content)
Puzzle 5: Append and Read 
Append "New data" to log.txt, then read the entire file.
with open('log.txt', 'a') as file:
    file.write("New data\n") 


with open('log.txt', 'r') as file:
    content = file.read()


print("Content of 'log.txt':")
print(content)
Puzzle 6: Write a List of Numbers to a File
Write numbers 1 to 5, each on a new line in numbers.txt.
with open('numbers.txt', 'w') as file:
   
    for number in range(1, 6):
        file.write(f"{number}\n")  

print("Numbers 1 to 5 written to 'numbers.txt' successfully.")
Puzzle 7: Read a File Line by Line
Read numbers.txt line by line and print each line.
with open('numbers.txt', 'r') as file:
  
    for line in file:
        print(line.strip())
Puzzle 8: Count the Number of Words in a File
Count the number of words in story.txt.
with open('story.txt', 'r') as file:
    text = file.read()


words = text.split()
word_count = len(words)

print(f"The number of words in the file is: {word_count}")
Puzzle 9: Find and Replace in a File
Replace "old" with "new" in data.txt.
with open('data.txt', 'r') as file:
    content = file.read()  


modified_content = content.replace("old", "new")


with open('data.txt', 'w') as file:
    file.write(modified_content)  

print("Replaced 'old' with 'new' in 'data.txt' successfully.")
Puzzle 10: Remove Blank Lines from a File
Remove all empty lines from text.txt.
with open('text.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Filter out empty lines
non_empty_lines = [line for line in lines if line.strip()]

# Open the file in write mode ('w') to overwrite it with non-empty lines
with open('text.txt', 'w') as file:
    file.writelines(non_empty_lines)  # Write the non-empty lines back to the file

print("Removed all empty lines from 'text.txt' successfully.")
Puzzle 11: Handle Division by Zero
Handle ZeroDivisionError when dividing numbers.
def divide_numbers():
    try:
       
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        
        result = numerator / denominator
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    else:
        print(f"The result of {numerator} divided by {denominator} is: {result}")


divide_numbers()
Puzzle 12: Handle Multiple Exceptions
Catch ValueError and ZeroDivisionError.
def divide_numbers():
    try:
        
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        
        result = numerator / denominator
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    else:
        print(f"The result of {numerator} divided by {denominator} is: {result}")

divide_numbers()
Puzzle 13: Use finally Block
Ensure "Execution completed" always prints.
def divide_numbers():
    try:
       
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    else:
        print(f"The result of {numerator} divided by {denominator} is: {result}")
    finally:
        print("Execution completed.")


divide_numbers()
Puzzle 14: Raise a Custom Exception
Raise an error if a number is negative.
def check_number(num):
    if num < 0:
        raise ValueError("Error: The number cannot be negative.")
    else:
        print(f"The number {num} is valid.")

# Example usage
try:
    number = float(input("Enter a number: "))
    check_number(number)
except ValueError as e:
    print(e)
    Puzzle 15: Handle File Not Found Exception
Handle a missing file error when reading a file.
def read_file(filename):
    try:
       
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filename = input("Enter the name of the file to read: ")
read_file(filename)
        
