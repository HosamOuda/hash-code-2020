class Library:
    def __init__(self, books: list, signup_days, shipment_per_day, index, books_scores: list):
        self.books: list = self.sort_book(books_scores, books)
        self.signup_days = signup_days
        self.shipment_per_day = shipment_per_day

        self.score = 0
        self.index = index

    def __lt__(self, other):
        return self.score < other.score

    def sort_book(self, books_scores: list, books: list):
        n = len(books)
        for i in range(n):
            for j in range(0, n - i - 1):
                if books_scores[books[j]] < books_scores[books[j + 1]]:
                    books[j], books[j + 1] = books[j + 1], books[j]

        return books
