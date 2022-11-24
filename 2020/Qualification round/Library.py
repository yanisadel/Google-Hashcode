class Library:
    def __init__(self, nb_books_available, signup_process_duration, nb_books_can_ship, books_in_library, id):
        self.id = id

        self.nb_books_available = nb_books_available 
        self.signup_process_duration = signup_process_duration
        self.nb_books_can_ship = nb_books_can_ship # Number of books that can be shipped per day

        self.has_signed_up = False

        self.books_in_library = books_in_library # List of books available in the library
        self.books_in_library.sort(key=lambda book: book.score)

        self.books_in_library_id = set(map(lambda book: book.id, books_in_library))

        self.score = self.get_score()

    def is_book_available(self, book_id):
        return book_id in self.books_in_library_id

    def get_score(self):
        res = 0
        for book in self.books_in_library:
            if condition(book, self.id):
                res += book.score
        
        return res

    def get_nb_books_still_available(self):
        res = 0
        for book in self.books_in_library:
            if condition(book, self.id):
                res += book.score
        
        return res

    def get_best_books_to_scan(self, nb_days=1):
        if nb_days <= 0:
            return []
        
        else:
            i = 0
            n = len(self.books_in_library)
            compteur = 0

            books_not_signed = []

            while (i < n) and (compteur < nb_days*self.nb_books_can_ship):
                book = self.books_in_library[i]
                if condition(book, self.id):
                    compteur += 1
                    books_not_signed.append(book)
                
                i += 1

            return books_not_signed

    def get_still_possible_score(self, nb_days_left=1):
        books_still_possible = self.get_best_books_to_scan(nb_days=nb_days_left)
        score = 0
        for book in books_still_possible:
            score += book.score
        
        return score

    
    def remove_useless_books(self):
        n = len(self.books_in_library)
        i = 0
        while i < n:
            if not condition(self.books_in_library[i], self.id):
                self.books_in_library.pop(i)
                i -= 1
                n -= 1
            
            i += 1



def condition(book, library_id):
    # False si le livre ne nous intéresse plus pour cette librairie
    if book.is_scanned():
        return False

    if book.will_be_scanned:
        if book.will_be_scanned_by_library != library_id:
            return False

    return True
