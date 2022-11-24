from Book import Book
from Library import Library

def get_data(PATH):
    with open(PATH, 'r') as f:
        nb_books, nb_libraries, nb_days = map(int, f.readline().strip().split())
        book_scores = list(map(int, f.readline().strip().split()))

        books = []
        for i, score in enumerate(book_scores):
            books.append(Book(i, score))

        libraries = []

        for i in range(nb_libraries):
            nb_books_available, signup_process_duration, nb_books_can_ship = map(int, f.readline().strip().split())
            books_in_library = list(map(int, f.readline().strip().split()))
            books_in_library = list(map(lambda i: books[i], books_in_library))

            library = Library(nb_books_available, signup_process_duration, nb_books_can_ship, books_in_library, i)
            libraries.append(library)

    return nb_books, nb_libraries, nb_days, books, libraries