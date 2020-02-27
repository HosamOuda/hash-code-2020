from models.library import Library


class FileManager:
    @staticmethod
    def read_file(file_name: str):
        libraries = []
        books_scores = []
        picked_books = []

        with open(file_name) as f:
            lines = [line.rstrip() for line in f]

        # number of different books
        B = int(lines[0].split(' ')[0])
        # number of libraries
        L = int(lines[0].split(' ')[1])
        # the number of days
        D = int(lines[0].split(' ')[2])

        # the scores of books line
        for item in lines[1].split():
            books_scores.append(int(item))
            picked_books.append(False)

        line_index = 2
        for library in range(L):
            library_props = lines[line_index].split(' ')
            library_books = lines[line_index + 1].split(' ')

            int_library_props = list(map(int, library_props))
            int_library_books = list(map(int, library_books))

            libraries.append(
                Library(int_library_books, int_library_props[1], int_library_props[2], library, books_scores))
            line_index += 2

        f.close()

        return B, L, D, libraries, books_scores, picked_books

    @staticmethod
    def write_file(file_name: str, output: list):
        f = open(file_name, "w")
        f.write(F"{len(output)}\n")
        for item in range(len(output)):
            f.write(
                f'{output[item].index} {len(output[item].books)} \n{" ".join(map(str, output[item].books))}\n')
        f.write('\n')
        f.close()
