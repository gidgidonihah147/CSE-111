import datetime
import json
import os

def add_book(library):
    """Adds a new book to the library with a timestamp."""
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    library.append({"title": title, "author": author, "genre": genre, "timestamp": timestamp})
    print("Book added successfully!")

def display_library(library):
    """Displays all books in the library."""
    if not library:
        print("Your library is empty.")
    else:
        for book in library:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Genre: {book['genre']}")
            print(f"Added on: {book['timestamp']}")
            print("---")

def search_book(library):
    """Searches for a book by title."""
    search_term = input("Enter the title of the book you're looking for: ")
    found_books = []
    for book in library:
        if search_term.lower() in book['title'].lower():
            found_books.append(book)

    if found_books:
        print("Found books:")
        display_library(found_books)
    else:
        print("No books found with that title.")

def save_library(library):
    """Saves the library to a JSON file in the local directory."""
    current_directory = os.getcwd()  # Get current directory
    filename = input("Enter the filename to save (e.g., library1, library2): ")
    filename += '.json'
    filepath = os.path.join(current_directory, filename)  # Combine directory and filename
    with open(filepath, 'w') as f:
        json.dump(library, f)
    print(f"Library saved to {filepath}")

def load_library():
    """Loads the library from a user-specified JSON file in the local directory,
    showing a list of available library files.
    """
    current_directory = os.getcwd()
    json_files = [f for f in os.listdir(current_directory) if f.endswith('.json')]
    if json_files:
        print("Available library files:")
        for i, f in enumerate(json_files):
            print(f"{i+1}. {f}")

        while True:
            try:
                file_index = int(input("Enter the number of the file to load: ")) - 1
                filename = json_files[file_index]
                filepath = os.path.join(current_directory, filename)
                with open(filepath, 'r') as f:
                    library = json.load(f)
                return library
            except (IndexError, ValueError):
                print("Invalid input. Please enter a valid number.")
            except json.JSONDecodeError:
                print("Invalid JSON file. Please try again.")
    else:
        print("No library files found in the current directory.")
        return []

def main():
    """Main function to run the program."""
    my_library = []

    while True:
        print("\n|-----------Options------------|")
        print("| 1. Add a book                |")
        print("| 2. Display library           |")
        print("| 3. Search for a book         |")
        print("| 4. Save library to a file    |")
        print("| 5. Load library from a file  |")
        print("| 6. Exit                      |")
        print("|------------------------------|")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book(my_library)
        elif choice == '2':
            display_library(my_library)
        elif choice == '3':
            search_book(my_library)
        elif choice == '4':
            save_library(my_library)
        elif choice == '5':
            my_library = load_library()
            print("Library loaded successfully!")
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()