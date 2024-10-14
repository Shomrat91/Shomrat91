class Library:
    def __init__(self, books=None):
        # Use an empty list if no initial books are provided
        self.books = books if books is not None else []
        self.no_of_books = len(self.books)

    def display_all_books(self):
        # Display the number of books and each book title
        print(f"There are {self.no_of_books} books in the library:")
        for book in self.books:
            print(f"> {book}")  

    def add_new_book(self):
        book_name = input("Enter the book name to add: ")  
        self.books.append(book_name)
        self.no_of_books += 1
        print(f"{book_name} has been added to the library.")

    def get_number_of_books(self):
        return self.no_of_books

def main():
    initial_books = []  # Keep initial_books empty or add some titles

    my_library = Library(initial_books)

    while True:
        method_choice = input("What do you want to do? (add/display/getNum/exit): ").strip().lower()

        if method_choice == 'add':
            my_library.add_new_book()

        elif method_choice == 'display':  
            my_library.display_all_books()

        elif method_choice == 'getnum':  # Lowercase for consistency
            print(f"Total number of books: {my_library.get_number_of_books()}")  

        elif method_choice == 'exit':
            print("Thanks! Goodbye.")
            break

        else:
            print("Invalid input, please try again.")  
if __name__ == "__main__":
    main()  # Call the main function when the script runs
