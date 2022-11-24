class Book:
    def __init__(self, id, score):
        self.id = id
        self.score = score
        self.scanned = False
        self.will_be_scanned = False
        self.will_be_scanned_by_library = None

    def is_scanned(self):
        return self.scanned

    def scan(self):
        self.scanned = True
