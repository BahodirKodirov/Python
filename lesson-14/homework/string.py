Task: JSON Parsing
write a Python script that reads the students.jon JSON file and prints details of each student.
Task: Weather API
Use this url : https://openweathermap.org/
Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
Task: JSON Modification
Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
Task: Movie Recommendation System
Use this url http://www.omdbapi.com/ to fetch information about movies.
Create a program that asks users for a movie genre and recommends a random movie from that genre.

  import json

def read_students_json():
    # Reading the JSON file
    with open('students.json', 'r') as file:
        students_data = json.load(file)

    # Printing student details
    for student in students_data:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
        print(f"Subjects: {', '.join(student['subjects'])}")
        print('-' * 40)

read_students_json()

[
  {
    "name": "John Doe",
    "age": 16,
    "grade": "10th",
    "subjects": ["Math", "Science", "English"]
  },
  {
    "name": "Jane Smith",
    "age": 15,
    "grade": "9th",
    "subjects": ["History", "Math", "Art"]
  }
]


import requests

def fetch_weather(city_name):
    # Replace with your OpenWeatherMap API key
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Construct the complete URL
    url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    
    # Make the API request
    response = requests.get(url)
    
    # If the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        main_data = data['main']
        weather_data = data['weather'][0]
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main_data['temp']}°C")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Weather: {weather_data['description']}")
        print(f"Pressure: {main_data['pressure']} hPa")
    else:
        print("City not found or error in API call")

fetch_weather('Tashkent')

import json

def load_books():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

def add_book():
    books = load_books()
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    
    new_book = {
        "title": title,
        "author": author,
        "year": year
    }
    
    books.append(new_book)
    save_books(books)
    print(f"Book '{title}' added successfully.")

def update_book():
    books = load_books()
    title = input("Enter the title of the book to update: ")
    
    for book in books:
        if book["title"].lower() == title.lower():
            new_author = input(f"Enter new author for '{title}': ")
            new_year = input(f"Enter new year for '{title}': ")
            book["author"] = new_author
            book["year"] = new_year
            save_books(books)
            print(f"Book '{title}' updated successfully.")
            return
    
    print(f"Book with title '{title}' not found.")

def delete_book():
    books = load_books()
    title = input("Enter the title of the book to delete: ")
    
    for book in books:
        if book["title"].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print(f"Book '{title}' deleted successfully.")
            return
    
    print(f"Book with title '{title}' not found.")

def main():
    while True:
        print("\n1. Add a book")
        print("2. Update a book")
        print("3. Delete a book")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

main()

[
    {
        "title": "1984",
        "author": "George Orwell",
        "year": "1949"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": "1960"
    }
]

import requests
import random

def get_movie_recommendation(genre):
    api_key = "your_api_key_here"
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}"

    # Fetching movies from OMDB API
    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        movies = data["Search"]
        if movies:
            # Randomly selecting a movie from the list
            recommended_movie = random.choice(movies)
            print(f"Recommended Movie: {recommended_movie['Title']}")
            print(f"Year: {recommended_movie['Year']}")
            print(f"IMDb ID: {recommended_movie['imdbID']}")
        else:
            print(f"No movies found for the genre '{genre}'.")
    else:
        print("Error fetching data from OMDB.")

def main():
    genre = input("Enter a movie genre (e.g., Action, Comedy, Drama): ")
    get_movie_recommendation(genre)

main()


