import pytest
import json
import os
from personal_library import add_book, search_book, load_library  # Import functions to test
import builtins  # Import the builtins module

def test_add_book(monkeypatch):
    """Tests adding a book with simulated user input."""

    # Sample book data
    book_data = {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "Science Fiction"
    }

    # Use monkeypatch to simulate user input
    inputs = [book_data["title"], book_data["author"], book_data["genre"]]
    monkeypatch.setattr(builtins, "input", lambda _: inputs.pop(0))

    # Initialize an empty library
    library = []

    # Call the add_book function
    add_book(library)

    # Assert that the book was added to the library
    assert len(library) == 1  # Check if the library has 1 book
    added_book = library[0]
    for key, value in book_data.items():
        assert added_book[key] == value  # Check if the book details are correct

def test_load_library(monkeypatch):  # Use monkeypatch fixture
    """
    Tests loading a library from 'exampleLibrary.json'.
    
    Uses monkeypatch to simulate user input.
    """

    # Load the expected data from the JSON file directly
    with open("exampleLibrary.json", "r") as f:
        expected_library = json.load(f)

    # Use monkeypatch to simulate user input
    monkeypatch.setattr(builtins, "input", lambda _: "1")  # Simulate entering "1"

    # Call the load_library function
    loaded_library = load_library()

    # Assert that the loaded library matches the expected library
    assert loaded_library == expected_library


def load_library_data(filename="exampleLibrary.json"):
    with open(filename, 'r') as f:
        return json.load(f)

# Pytest function to test the search_book function
def test_search_book(monkeypatch):
    library = load_library_data()
    # Simulate user input for the search term
    search_term = "Harry Potter"  
    monkeypatch.setattr('builtins.input', lambda _: search_term)
    
    # Capture the printed output of the search_book function
    import io
    from contextlib import redirect_stdout

    f = io.StringIO()
    with redirect_stdout(f):
        search_book(library)  # Call the function with the test data
    out = f.getvalue()

    # Assert that the output contains the expected book title
    assert "Harry Potter and the Sorcerer's Stone" in out

    
if __name__ == '__main__':
    pytest.main()
