from utils.file_manager import FileManager
from utils.engine import Engine

B, L, D, libraries, books_scores, picked_books = FileManager.read_file('a_example.txt')


engine = Engine(libraries=libraries, D=D, books_scores=books_scores, picked_books=picked_books)
output: list = engine.start()

FileManager.write_file('a.txt', output)
