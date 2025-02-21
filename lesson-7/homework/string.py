•	1. Write a function `greet()` that prints 'Hello, World!' when called.
def greet():
    print('Hello world')

greet() 

•	2. Create a function `show_date_time()` that prints the current date and time.
from datetime import datetime

def show_date_time():
    current_time = datetime.now() 
    print("Current date and time:", current_time)


show_date_time()
•	3. Write a function `display_even_numbers()` that prints even numbers from 1 to 20.
def display_even_numbers():
    for number in range(1, 21):  
        if number % 2 == 0: 
            print(number)  


display_even_numbers()


•	4. Write a function `greet_user(name)` that takes a name as a parameter and prints 'Hello, [name]!'

def greet_user(name):
    print(f"Hello, {name}!")  


greet_user("Alice")
greet_user("Bob")
•	5. Create a function `print_square(n)` that prints the square of a given number.
def print_square(n):
    square = n ** 2  
    print(f"The square of {n} is {square}.") 


print_square(4)
print_square(7)

•	6. Write a function `multiply_numbers(a, b)` that takes two numbers and prints their product.
def multiply_numbers(a, b):
    product = a * b
    print("The product of", a, "and", b, "is:", product)


multiply_numbers(5, 3) 
•	7. Write a function `get_pi()` that returns the value of π (3.14159).
def get_pi():
    return 3.14159


pi_value = get_pi()
print("The value of π is:", pi_value)
•	8. Create a function `random_number()` that returns a random number between 1 and 100.
import random

def random_number():
    return random.randint(1, 100)

random_value = random_number()
print("Random number between 1 and 100:", random_value)
•	9. Write a function `current_year()` that returns the current year.
import datetime

def current_year():
    return datetime.datetime.now().year


year = current_year()
print("The current year is:", year)
•	10. Write a function `add_numbers(a, b)` that returns the sum of two numbers.
def add_numbers(a, b):
    result=a+b
    print(f" Matija {a} + {b} = {result} ")

add_numbers(1,2)  
•	11. Create a function `is_even(n)` that returns `True` if the number is even and `False` otherwise.
def is_even(n):
    return n % 2 == 0

number = 4
if is_even(number):
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
  •	12. Write a function `get_factorial(n)` that returns the factorial of a given number.
def get_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial


number = 2

result = get_factorial(number)
print(f"The factorial of {number} is: {result}")
•	13. Write a recursive function `countdown(n)` that prints numbers from `n` to `1`.
def countdown(n):
    if n <= 0:
        return  
    print(n) 
    countdown(n - 1)  


countdown(5)
•	14. Create a recursive function `sum_natural(n)` that returns the sum of the first `n` natural numbers.
def sum_natural(n):
    if n <= 0:
        return 0 
    else:
        return n + sum_natural(n - 1) 

number = 5
result = sum_natural(number)
print(f"The sum of the first {number} natural numbers is: {result}")
•	15. Write a recursive function `fibonacci(n)` that returns the `n`th Fibonacci number.
def fibonacci(n):
    if n < 0:
        return "Invalid input"  
    elif n == 0:
        return 0  
    elif n == 1:
        return 1 
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  


number = 6
result = fibonacci(number)
print(f"The {number}th Fibonacci number is: {result}")
•	16. Write a function `sum_numbers(*args)` that takes multiple numbers and returns their sum.
def sum_numbers(*args):
    return sum(args) 


result = sum_numbers(1, 2, 3, 4, 5)
print("The sum of the numbers is:", result) 
•	17. Create a function `print_info(**kwargs)` that prints key-value pairs passed as arguments.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=30, city="New York", country="USA")
•	18. Write a function `power(base, exponent=2)` that returns `base` raised to the power of `exponent`.
def power(base, exponent=2):
    return base ** exponent  


result1 = power(3) 
result2 = power(3, 3)  

print("3 raised to the power of 2 is:", result1)  
print("3 raised to the power of 3 is:", result2)
•	19. Create a function `calculate_area(length: float, width: float) -> float` that returns the area of a rectangle. Add a docstring explaining the function.
def calculate_area(length: float, width: float) -> float:
   
    return length * width

area = calculate_area(5.0, 3.0)
print("The area of the rectangle is:", area)
•	20. Given a list of numbers, use `map()` to square each number and use `filter()` to return only the even squares. Write a function `process_numbers(nums: list) -> list`.
def process_numbers(nums: list) -> list:

    squared_numbers = map(lambda x: x ** 2, nums)
    
   
    even_squares = filter(lambda x: x % 2 == 0, squared_numbers)
    
  
    return list(even_squares)

numbers = [1, 2, 3, 4, 5, 6]
result = process_numbers(numbers)
print("Even squares:", result)
•	21. Write a function `reverse_string(s: str) -> str` that returns the reversed version of a given string.
def reverse_string(s: str) -> str:

    return s[::-1]  


input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string) 
•	22. Create a function `count_vowels(s: str) -> int` that returns the number of vowels in a given string.
def count_vowels(s: str) -> int:
 
    vowels = "aeiouAEIOU"  
    count = sum(1 for char in s if char in vowels)  
    return count


input_string = "Hello, World!"
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)
•	23. Write a recursive function `gcd(a, b)` to find the greatest common divisor of two numbers.
def gcd(a: int, b: int) -> int:
  
    if b == 0:
        return a 
    else:
        return gcd(b, a % b)  

num1 = 48
num2 = 18
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")
•	24. Implement a function `merge_lists(*lists)` that takes multiple lists as arguments and returns a single merged list.
def merge_lists(*lists):
   
    merged_list = []
    for lst in lists:
        merged_list.extend(lst)  
    return merged_list


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]
result = merge_lists(list1, list2, list3)
print("Merged list:", result)
•	25. Write a function `student_data(name, age=18, **details)` that takes a name and age (default 18) and prints additional details from `**details`.
  def student_data(name: str, age: int = 18, **details):
  
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    
    if details:
        print("Additional Details:")
        for key, value in details.items():
            print(f"{key}: {value}")


student_data("Alice", 20, major="Computer Science", grade="A", hobbies=["reading", "coding"])
•	26. Create a function `calculate_interest(principal: float, rate: float = 5.0, time: int = 1) -> float` that returns the calculated simple interest.
def calculate_interest(principal: float, rate: float = 5.0, time: int = 1) -> float:
    """
    Calculate the simple interest.

    Parameters:
    principal (float): The principal amount.
    rate (float): The interest rate (default is 5.0).
    time (int): The time period in years (default is 1).

    Returns:
    float: The calculated simple interest.
    """
    interest = (principal * rate * time) / 100  # Calculate simple interest
    return interest

# Example usage:
principal_amount = 1000.0
interest_rate = 5.0
time_period = 2
interest = calculate_interest(principal_amount, interest_rate, time_period)
print(f"The calculated interest is: {interest}")
•	27. Use `map()` to convert a list of Fahrenheit temperatures to Celsius.
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * 5 / 9

# List of Fahrenheit temperatures
fahrenheit_temps = [32, 68, 100, 212, 50]

# Use map to convert the list of Fahrenheit temperatures to Celsius
celsius_temps = list(map(fahrenheit_to_celsius, fahrenheit_temps))

# Print the results
print("Fahrenheit temperatures:", fahrenheit_temps)
print("Celsius temperatures:", celsius_temps)
•	28. Use `filter()` to extract all prime numbers from a given list.
def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # n is divisible by i, so it's not prime
    return True  # n is prime

# Given list of numbers
numbers = [10, 15, 3, 7, 8, 23, 4, 5, 11, 13, 17]

# Use filter to extract prime numbers from the list
prime_numbers = list(filter(is_prime, numbers))

# Print the results
print("Original numbers:", numbers)
print("Prime numbers:", prime_numbers)
•	29. Write a function `calculate_discount(price: float, discount: float = 10.0) -> float` that returns the final price after applying a percentage discount.
def calculate_discount(price: float, discount: float = 10.0) -> float:
    """
    Calculate the final price after applying a discount.

    Parameters:
    price (float): The original price of the item.
    discount (float): The discount percentage to apply (default is 10.0).

    Returns:
    float: The final price after applying the discount.
    """
    discount_amount = (price * discount) / 100  # Calculate the discount amount
    final_price = price - discount_amount  # Subtract the discount from the original price
    return final_price

# Example usage:
original_price = 100.0
discount_percentage = 15.0
final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after a {discount_percentage}% discount is: ${final_price:.2f}") 
•	30. Write a function `unique_words(sentence: str) -> set` that returns a set of unique words from a given sentence.
def unique_words(sentence: str) -> set:
    """
    Extract unique words from a given sentence.

    Parameters:
    sentence (str): The input sentence from which to extract unique words.

    Returns:
    set: A set of unique words from the input sentence.
    """
    # Split the sentence into words and convert to lowercase for uniformity
    words = sentence.lower().split()
    
    # Use a set to get unique words
    unique_word_set = set(words)
    
    return unique_word_set

# Example usage:
input_sentence = "This is a test sentence and this is only a test."
unique_word_set = unique_words(input_sentence)
print("Unique words:", unique_word_set)
