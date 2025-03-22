Homework:

Exercise 1: Threaded Prime Number Checker

Write a Python program that checks whether a given range of numbers contains prime numbers. Divide the range among multiple threads to parallelize the prime checking process. Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

Exercise 2: Threaded File Processing

Write a program that reads a large text file containing lines of text. Implement a threaded solution to count the occurrence of each word in the file. Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.
import threading
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check prime numbers in a given range
def check_primes(start, end, prime_list):
    for num in range(start, end):
        if is_prime(num):
            prime_list.append(num)

# Main function
def threaded_prime_checker(start, end, num_threads):
    # Divide the range into chunks for each thread
    step = (end - start) // num_threads
    threads = []
    prime_list = []

    # Create threads
    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = start + (i + 1) * step if i != num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, prime_list))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print the primes found
    print("Prime numbers found:", sorted(prime_list))

# Example usage
start = 1
end = 100
num_threads = 4
threaded_prime_checker(start, end, num_threads)

import threading
from collections import defaultdict

# Function to count words in a chunk of text
def count_words_in_chunk(start, end, file_path, word_count):
    with open(file_path, 'r') as file:
        file.seek(start)
        chunk = file.read(end - start)
        words = chunk.split()
        for word in words:
            word_count[word.lower()] += 1

# Function to get the file size
def get_file_size(file_path):
    with open(file_path, 'rb') as file:
        file.seek(0, 2)  # Move to the end of the file
        return file.tell()

# Main function for threaded word counting
def threaded_word_counter(file_path, num_threads):
    file_size = get_file_size(file_path)
    step = file_size // num_threads
    threads = []
    word_count = defaultdict(int)

    # Create threads to process the file in chunks
    for i in range(num_threads):
        thread_start = i * step
        thread_end = (i + 1) * step if i != num_threads - 1 else file_size
        thread = threading.Thread(target=count_words_in_chunk, args=(thread_start, thread_end, file_path, word_count))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Print the word count summary
    print("Word occurrences:")
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")

# Example usage
file_path = 'large_text_file.txt'  # Replace with the path to your large text file
num_threads = 4
threaded_word_counter(file_path, num_threads)

