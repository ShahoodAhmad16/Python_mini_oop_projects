class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self):
        print(f'''Title: {self.title}
Author: {self.author}
Year: {self.year}
''')

    def is_available(self):
        print(f'Is Availaible')


class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def info(self):
        super().info()
        print(f'Pages: {self.pages}')


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def info(self):
        super().info()
        print(f'Issue Number {self.issue_number}')


library_collection: list[LibraryItem] = [
    Book('Reham Khan', 'Reham Khan', 2019, 500),
    Magazine('World Times', 'Pakistan', 2000, 123)
]

for library in library_collection:
    library.info()
    library.is_available()
    print('*'.center(20, '-'))
