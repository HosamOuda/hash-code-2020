import heapq


class Engine:
    def __init__(self, libraries: list, D: int, books_scores: list, picked_books: list):
        self.start_day = 0
        self.libraries = libraries
        self.books_scores = books_scores
        self.picked_books = picked_books
        self.D = D

    def start(self):
        output = []
        while (self.start_day < self.D) and (len(self.libraries) != 0):

            self.calculate_score(self.libraries, self.books_scores, self.picked_books)

            heapq._heapify_max(self.libraries)
            temp = heapq.heappop(self.libraries)
            output.append(temp)

            self.start_day += temp.signup_days
            for j in range(len(temp.books)):
                self.picked_books[temp.books[j]] = True

        return output

    def calculate_score(self, library: list, books, owned_books):
        for i in range(len(library)):
            library_book_score = 0
            for j in range(len(library[i].books)):
                if not (owned_books[library[i].books[j]]):
                    library_book_score = library_book_score + books[library[i].books[j]]  # index
            library_score = library_book_score / float(library[i].signup_days)
            library[i].score = library_score
