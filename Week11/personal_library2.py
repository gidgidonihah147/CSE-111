import datetime
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox

def add_book(library):
    """Adds a new book to the library with a timestamp."""
    def add_to_library():
        title = title_entry.get()
        author = author_entry.get()
        genre = genre_entry.get()
        if title and author and genre:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            library.append({"title": title, "author": author, "genre": genre, "timestamp": timestamp})
            messagebox.showinfo("Success", "Book added successfully!")
            title_entry.delete(0, tk.END)
            author_entry.delete(0, tk.END)
            genre_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    add_window = tk.Toplevel(root)
    add_window.title("Add Book")

    title_label = ttk.Label(add_window, text="Title:")
    title_label.grid(row=0, column=0, padx=5, pady=5)
    title_entry = ttk.Entry(add_window)
    title_entry.grid(row=0, column=1, padx=5, pady=5)

    author_label = ttk.Label(add_window, text="Author:")
    author_label.grid(row=1, column=0, padx=5, pady=5)
    author_entry = ttk.Entry(add_window)
    author_entry.grid(row=1, column=1, padx=5, pady=5)

    genre_label = ttk.Label(add_window, text="Genre:")
    genre_label.grid(row=2, column=0, padx=5, pady=5)
    genre_entry = ttk.Entry(add_window)
    genre_entry.grid(row=2, column=1, padx=5, pady=5)

    add_button = ttk.Button(add_window, text="Add Book", command=add_to_library)
    add_button.grid(row=3, column=1, padx=5, pady=5)

def display_library(library):
    """Displays all books in the library."""
    display_window = tk.Toplevel(root)
    display_window.title("Library")

    if not library:
        ttk.Label(display_window, text="Your library is empty.").pack(padx=5, pady=5)
    else:
        text_area = tk.Text(display_window, wrap=tk.WORD)
        text_area.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        for book in library:
            text_area.insert(tk.END, f"Title: {book['title']}\n")
            text_area.insert(tk.END, f"Author: {book['author']}\n")
            text_area.insert(tk.END, f"Genre: {book['genre']}\n")
            text_area.insert(tk.END, f"Added on: {book['timestamp']}\n")
            text_area.insert(tk.END, "---\n")
        text_area.config(state=tk.DISABLED)  # Make the text area read-only

def search_book(library):
    """Searches for a book by title."""
    def search_and_display():
        search_term = search_entry.get()
        found_books = []
        for book in library:
            if search_term.lower() in book['title'].lower():
                found_books.append(book)

        if found_books:
            display_library(found_books)  # Reuse display_library for consistent output
        else:
            messagebox.showinfo("Search Results", "No books found with that title.")

    search_window = tk.Toplevel(root)
    search_window.title("Search Book")

    search_label = ttk.Label(search_window, text="Enter title:")
    search_label.grid(row=0, column=0, padx=5, pady=5)
    search_entry = ttk.Entry(search_window)
    search_entry.grid(row=0, column=1, padx=5, pady=5)

    search_button = ttk.Button(search_window, text="Search", command=search_and_display)
    search_button.grid(row=1, column=1, padx=5, pady=5)

def save_library(library):
    """Saves the library to a JSON file in the local directory."""
    def save_to_file():
        filename = filename_entry.get()
        if filename:
            filepath = os.path.join(os.getcwd(), filename + ".json")
            with open(filepath, 'w') as f:
                json.dump(library, f)
            messagebox.showinfo("Success", f"Library saved to {filepath}")
            filename_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a filename.")

    save_window = tk.Toplevel(root)
    save_window.title("Save Library")

    filename_label = ttk.Label(save_window, text="Filename:")
    filename_label.grid(row=0, column=0, padx=5, pady=5)
    filename_entry = ttk.Entry(save_window)
    filename_entry.grid(row=0, column=1, padx=5, pady=5)

    save_button = ttk.Button(save_window, text="Save", command=save_to_file)
    save_button.grid(row=1, column=1, padx=5, pady=5)

def load_library():
    """Loads the library from a user-specified JSON file in the local directory."""
    global my_library

    def load_from_file(event=None):
        global my_library
        filename = filename_var.get()
        if filename:
            filepath = os.path.join(os.getcwd(), filename)
            try:
                with open(filepath, "r") as f:
                    library = json.load(f)
                messagebox.showinfo("Success", "Library loaded successfully!")
                current_file_label.config(text=f"Current File: {filename}")
                my_library = library  # Update the main library variable
            except FileNotFoundError:
                messagebox.showerror("Error", "File not found.")
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Invalid JSON file.")
        else:
            messagebox.showerror("Error", "Please select a filename.")

    load_window = tk.Toplevel(root)
    load_window.title("Load Library")

    current_directory = os.getcwd()
    json_files = [f for f in os.listdir(current_directory) if f.endswith(".json")]
    if not json_files:
        messagebox.showerror("Error", "No JSON files found in the current directory.")
        return

    filename_var = tk.StringVar(load_window)
    filename_var.set(json_files[0])  # Set the default value

    filename_dropdown = ttk.Combobox(
        load_window, textvariable=filename_var, values=json_files
    )
    filename_dropdown.grid(row=0, column=0, padx=5, pady=5)
    filename_dropdown.bind(
        "<<ComboboxSelected>>", load_from_file
    )  # Bind the event to the function

    load_button = ttk.Button(load_window, text="Load", command=load_from_file)
    load_button.grid(row=1, column=0, padx=5, pady=5)

def main():
    """Main function to run the program."""
    global my_library, root, current_file_label

    try:
        with open("exampleLibrary.json", "r") as f:
            my_library = json.load(f)
        current_file = "exampleLibrary.json"
    except FileNotFoundError:
        my_library = []
        current_file = "No file loaded"

    root = tk.Tk()
    root.title("Personal Library")


    # Add a label to display the current filename
    current_file_label = ttk.Label(root, text=f"Current File: {current_file}")
    current_file_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Frame to hold the dynamic content
    content_frame = ttk.Frame(root)
    content_frame.grid(row=2, column=0, columnspan=12, padx=10, pady=10) 

    def clear_content_frame():
        """Clears the content frame."""
        for widget in content_frame.winfo_children():
            widget.destroy()

    def add_book_gui(library):
        """GUI for adding a book."""
        clear_content_frame()

        def add_to_library():
            title = title_entry.get()
            author = author_entry.get()
            genre = genre_entry.get()
            if title and author and genre:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                library.append(
                    {
                        "title": title,
                        "author": author,
                        "genre": genre,
                        "timestamp": timestamp,
                    }
                )
                messagebox.showinfo("Success", "Book added successfully!")
                title_entry.delete(0, tk.END)
                author_entry.delete(0, tk.END)
                genre_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Please fill in all fields.")

        title_label = ttk.Label(content_frame, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5)
        title_entry = ttk.Entry(content_frame)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        author_label = ttk.Label(content_frame, text="Author:")
        author_label.grid(row=1, column=0, padx=5, pady=5)
        author_entry = ttk.Entry(content_frame)
        author_entry.grid(row=1, column=1, padx=5, pady=5)

        genre_label = ttk.Label(content_frame, text="Genre:")
        genre_label.grid(row=2, column=0, padx=5, pady=5)
        genre_entry = ttk.Entry(content_frame)
        genre_entry.grid(row=2, column=1, padx=5, pady=5)

        add_button = ttk.Button(
            content_frame, text="Add Book", command=add_to_library
        )
        add_button.grid(row=3, column=1, padx=5, pady=5)

    def display_library_gui(library):
        """GUI for displaying the library."""
        clear_content_frame()
        
        if not library:
            ttk.Label(content_frame, text="Your library is empty.").pack(padx=5, pady=5)
        else:
            text_area = tk.Text(content_frame, wrap=tk.WORD)
            text_area.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
            for book in library:
                text_area.insert(tk.END, f"Title: {book['title']}\n")
                text_area.insert(tk.END, f"Author: {book['author']}\n")
                text_area.insert(tk.END, f"Genre: {book['genre']}\n")
                text_area.insert(tk.END, f"Added on: {book['timestamp']}\n")
                text_area.insert(tk.END, "---\n")
            text_area.config(state=tk.DISABLED)
        

    def search_book_gui(library):
        """GUI for searching for a book."""
        clear_content_frame()

        def search_and_display():
            search_term = search_entry.get()
            found_books = []
            for book in library:
                if search_term.lower() in book["title"].lower():
                    found_books.append(book)

            if found_books:
                display_library_gui(
                    found_books
                )  # Reuse display_library_gui for consistent output
            else:
                messagebox.showinfo("Search Results", "No books found with that title.")

        search_label = ttk.Label(content_frame, text="Enter title:")
        search_label.grid(row=0, column=0, padx=5, pady=5)
        search_entry = ttk.Entry(content_frame)
        search_entry.grid(row=0, column=1, padx=5, pady=5)

        search_button = ttk.Button(
            content_frame, text="Search", command=search_and_display
        )
        search_button.grid(row=1, column=1, padx=5, pady=5)

    def save_library_gui(library):
        # """GUI for saving the library."""
        clear_content_frame()

        def save_to_file():
            nonlocal library  # Add this line to access the library variable
            filename = filename_entry.get()
            if filename:
                filepath = os.path.join(os.getcwd(), filename + ".json")
                with open(filepath, "w") as f:
                    json.dump(library, f)
                messagebox.showinfo("Success", f"Library saved to {filepath}")
                filename_entry.delete(0, tk.END)
                current_file_label.config(text=f"Current File: {filename}.json")
            else:
                messagebox.showerror("Error", "Please enter a filename.")

        def update_current_file():
            nonlocal library  # Add this line to access the library variable
            current_file = current_file_label.cget("text").split(": ")[1]
            if current_file == "No file loaded":
                messagebox.showerror("Error", "No file loaded to update.")
                return
            filepath = os.path.join(os.getcwd(), current_file)
            with open(filepath, "w") as f:
                json.dump(library, f)
            messagebox.showinfo("Success", f"Current library updated in {current_file}")

        filename_label = ttk.Label(content_frame, text="Filename:")
        filename_label.grid(row=0, column=0, padx=5, pady=5)
        filename_entry = ttk.Entry(content_frame)
        filename_entry.grid(row=0, column=1, padx=5, pady=5)

        save_button = ttk.Button(content_frame, text="Save As", command=save_to_file)
        save_button.grid(row=1, column=1, padx=5, pady=5)

        update_button = ttk.Button(content_frame, text="Update Current", command=update_current_file)
        update_button.grid(row=2, column=1, padx=5, pady=5)

    def load_library_gui():
        """GUI for loading the library."""
        global my_library
        clear_content_frame()

        def load_from_file(event=None):
            global my_library
            filename = filename_var.get()
            if filename:
                filepath = os.path.join(os.getcwd(), filename)
                try:
                    with open(filepath, "r") as f:
                        library = json.load(f)
                    messagebox.showinfo("Success", "Library loaded successfully!")
                    current_file_label.config(text=f"Current File: {filename}")
                    my_library = library  # Update the main library variable
                except FileNotFoundError:
                    messagebox.showerror("Error", "File not found.")
                except json.JSONDecodeError:
                    messagebox.showerror("Error", "Invalid JSON file.")
            else:
                messagebox.showerror("Error", "Please select a filename.")

        current_directory = os.getcwd()
        json_files = [""] + [f for f in os.listdir(current_directory) if f.endswith(".json")]
        if not json_files:
            messagebox.showerror("Error", "No JSON files found in the current directory.")
            return

        filename_var = tk.StringVar(content_frame)
        filename_var.set(json_files[0])  # Set the default value

        filename_dropdown = ttk.Combobox(content_frame, textvariable=filename_var, values=json_files)
        filename_dropdown.grid(row=0, column=0, padx=5, pady=5)
        filename_dropdown.bind("<<ComboboxSelected>>", load_from_file)

        load_button = ttk.Button(content_frame, text="Load", command=load_from_file)
        load_button.grid(row=1, column=0, padx=5, pady=5)

    # Add Book button with "+" symbol
    add_button = ttk.Button(
        root, text="Add Book  +", command=lambda: add_book_gui(my_library)
    )
    add_button.grid(row=1, column=0, padx=10, pady=10)

    # Display Library button with "📖" (open book) symbol
    display_button = ttk.Button(
        root,
        text="Display Library  📖",
        command=lambda: display_library_gui(my_library),
    )
    display_button.grid(row=1, column=1, padx=10, pady=10)

    # Search Book button with "🔍" (magnifying glass) symbol
    search_button = ttk.Button(
        root, text="Search Book  🔍", command=lambda: search_book_gui(my_library)
    )
    search_button.grid(row=1, column=2, padx=10, pady=10)

    # Save Library button with "💾" (floppy disk) symbol
    save_button = ttk.Button(
        root,
        text="Save Library  💾",
        command=lambda: save_library_gui(my_library),
    )
    save_button.grid(row=1, column=3, padx=10, pady=10)

    # Load Library button with "📂" (open file folder) symbol
    load_button = ttk.Button(
        root, text="Load Library  📂", command=lambda: load_library_gui()
    )
    load_button.grid(row=1, column=4, padx=10, pady=10)

    # Calculate the width of the content_frame when "Display Library" is pressed
    display_library_gui(my_library)
    content_frame.update_idletasks()
    content_width = content_frame.winfo_width()
    clear_content_frame()
    total_width = content_width + 20  # Add 20 for the padding on both sides

    # Set the width of the root window and make it non-resizable
    root.geometry(f"{content_width}x{root.winfo_height()}")
    root.resizable(False, True)  # Disable resizing

    # Center the window on the screen
    root.update_idletasks()  # Update the window to get its actual size
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - total_width) // 2
    y = (screen_height - root.winfo_height()) // 2
    root.geometry(f"+{x}+{y}")

    root.mainloop()

if __name__ == "__main__":
    main()


