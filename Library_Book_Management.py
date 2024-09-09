# Define the class MyLibrary
class MyLibrary:
    def __init__(self):
        # Initialize an empty dictionary to store books
        self.books = {}

    # Method to add a new book
    def add_book(self, title, author):
        self.books[title] = {"Author": author, "Slot": "available"}
        print(f"Book '{title}' by {author} added to the library.")

    # Method to display all books
    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for key, value in self.books.items():
                print(f"{key} - Author: {value['Author']}, Status: {value['Slot']}")


# Create an instance of the class MyLibrary
my_library = MyLibrary()

# Add sample books to the library
my_library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
my_library.add_book("Moby Dick", "Herman Melville")
my_library.add_book("Pride and Prejudice", "Jane Austen")
my_library.add_book("The Hobbit", "J.R.R. Tolkien")
my_library.add_book("War and Peace", "Leo Tolstoy")
my_library.add_book("The Catcher in the Rye", "J.D. Salinger")
my_library.add_book("To Kill a Mockingbird", "Harper Lee")
my_library.add_book("1984", "George Orwell")
my_library.add_book("Brave New World", "Aldous Huxley")
my_library.add_book("The Odyssey", "Homer")

# Display all books in the library
my_library.display_books()
