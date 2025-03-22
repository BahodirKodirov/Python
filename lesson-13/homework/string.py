Homework:

Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

from datetime import datetime

def calculate_age():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    
    today = datetime.today()
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    # Adjust for negative values (e.g., if the birthday hasn't occurred yet this year)
    if age_days < 0:
        age_months -= 1
        age_days += (today - datetime(today.year, today.month, 1)).days
    
    if age_months < 0:
        age_years -= 1
        age_months += 12

    print(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")

calculate_age()

    from datetime import datetime

def days_until_birthday():
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
    
    today = datetime.today()
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)

    # If the birthday has already passed this year, calculate the next year's birthday
    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

    days_left = (next_birthday - today).days
    print(f"There are {days_left} days left until your next birthday.")

days_until_birthday()


from datetime import datetime, timedelta

def meeting_scheduler():
    current_time_str = input("Enter the current date and time (YYYY-MM-DD HH:MM): ")
    current_time = datetime.strptime(current_time_str, "%Y-%m-%d %H:%M")
    
    duration_hours = int(input("Enter the duration of the meeting in hours: "))
    duration_minutes = int(input("Enter the duration of the meeting in minutes: "))
    
    end_time = current_time + timedelta(hours=duration_hours, minutes=duration_minutes)
    print(f"The meeting will end at {end_time.strftime('%Y-%m-%d %H:%M')}.")

meeting_scheduler()


from datetime import datetime
import pytz

def timezone_converter():
    date_time_str = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
    current_timezone = input("Enter your current timezone (e.g., 'US/Eastern'): ")
    target_timezone = input("Enter the target timezone (e.g., 'Europe/London'): ")

    date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M")
    
    # Convert to the current timezone and then to the target timezone
    local_tz = pytz.timezone(current_timezone)
    target_tz = pytz.timezone(target_timezone)

    local_time = local_tz.localize(date_time)
    target_time = local_time.astimezone(target_tz)

    print(f"The time in {target_timezone} will be: {target_time.strftime('%Y-%m-%d %H:%M')}.")

timezone_converter()


import time
from datetime import datetime

def countdown_timer():
    future_date_str = input("Enter the future date and time (YYYY-MM-DD HH:MM): ")
    future_date = datetime.strptime(future_date_str, "%Y-%m-%d %H:%M")
    
    while True:
        remaining_time = future_date - datetime.now()
        if remaining_time.total_seconds() <= 0:
            print("Time's up!")
            break
        print(f"Time remaining: {str(remaining_time).split('.')[0]}", end='\r')
        time.sleep(1)

countdown_timer()


import re

def email_validator():
    email = input("Enter your email address: ")
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    if re.match(email_pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

email_validator()


def phone_number_formatter():
    phone_number = input("Enter your phone number (10 digits): ")
    
    if len(phone_number) == 10 and phone_number.isdigit():
        formatted_phone_number = f"({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}"
        print(f"Formatted phone number: {formatted_phone_number}")
    else:
        print("Invalid phone number. Please enter exactly 10 digits.")

phone_number_formatter()


import re

def password_strength_checker():
    password = input("Enter your password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
    elif not re.search(r'[A-Z]', password):
        print("Password must contain at least one uppercase letter.")
    elif not re.search(r'[a-z]', password):
        print("Password must contain at least one lowercase letter.")
    elif not re.search(r'[0-9]', password):
        print("Password must contain at least one digit.")
    else:
        print("Password is strong.")

password_strength_checker()

def word_finder():
    text = input("Enter a sample text: ")
    word_to_find = input("Enter the word to search for: ")

    occurrences = [i for i, word in enumerate(text.split()) if word.lower() == word_to_find.lower()]
    
    if occurrences:
        print(f"The word '{word_to_find}' was found at positions: {occurrences}")
    else:
        print(f"The word '{word_to_find}' was not found.")

word_finder()


import re

def date_extractor():
    text = input("Enter some text: ")

    # Regex to extract dates in the format YYYY-MM-DD
    date_pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    dates = re.findall(date_pattern, text)
    
    if dates:
        print("Dates found in the text:", dates)
    else:
        print("No dates found in the text.")

date_extractor()

