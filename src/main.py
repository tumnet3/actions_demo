class book:
    def __init__(self,title,author,year,available=True):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = available
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_year(self):
        return self.__year
    def is_available(self):
        return self.__available
    def mark_as_taken(self):
        self.__available = False
    def mark_as_returned(self):
        self.__available = True
    def __str__(self):
        status="Dostupna" if self.__available else "Nie dostupna"
        return f"{self.__title}, {self.__author}, {self.__year}, {status}"



class PrintedBook(book):
    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition

    def repair(self):
        if self.condition == "плохая":
            self.condition = "хорошая"
        elif self.condition == "хорошая":
            self.condition = "новая"

    def __str__(self):
        s = super().__str__()
        return f"{s}; {self.pages} стр, состояние: {self.condition}"



class EBook(book):
    def __init__(self, title, author, year, file_size, format_):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = format_

    def download(self):
        print(f"{self.get_title()} загружается")

    def __str__(self):
        s = super().__str__()
        return f"{s}; файл {self.file_size} МБ ({self.format})"




class User:
    def __init__(self, name):
        self.name = name
        self.__borrowed_books = []

    def borrow(self, book):
        if book.is_available():
            book.mark_as_taken()
            self.__borrowed_books.append(book)
            print(f"{self.name} вял «{book.get_title()}»")
        else:
            print(f"Книга «{book.get_title()}» недоступна")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.mark_as_returned()
            self.__borrowed_books.remove(book)
            print(f"{self.name} вернул «{book.get_title()}».")
        else:
            print(f"не у {self.name}")

    def show_books(self):
        if not self.__borrowed_books:
            print(f"{self.name} не брал")
        else:
            print(f"Книги {self.name}:")
            for b in self.__borrowed_books:
                print(b.get_title())

    def get_borrowed_books(self):
        return tuple(self.__borrowed_books)



class Librarian(User):
    def add_book(self, library, book):
        library.add_book(book)
        print(f"Библиотекарь добавил: {book.get_title()}")

    def remove_book(self, library, title):
        library.remove_book(title)
        print(f"Библиотекарь удалил {title}")

    def register_user(self, library, user):
        library.add_user(user)
        print(f"Пользователь {user.name} зареган.")


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []



    def add_book(self, book):
        self.__books.append(book)

    def remove_book(self, title):
        for b in self.__books:
            if b.get_title() == title:
                self.__books.remove(b)
                return True
        print("Книга не найдена.")
        return False

    def find_book(self, title):
        for book in self.__books:
            if book.get_title() == title:
                return book
        return None

    def show_all_books(self):
        print("Все книги:")
        for b in self.__books:
            print(b)

    def show_available_books(self):
        print("Доступные книги:")
        for b in self.__books:
            if b.is_available():
                print(b)



    def add_user(self, user):
        self.__users.append(user)

    def get_user(self, name):
        for u in self.__users:
            if u.name == name:
                return u
        return None



    def lend_book(self, title, user_name):
        user = self.get_user(user_name)
        if not user:
            print("Пользователь не найден.")
            return

        book = self.find_book(title)
        if not book:
            print("Книга не найдена.")
            return

        user.borrow(book)

    def return_book(self, title, user_name):
        user = self.get_user(user_name)
        if not user:
            print("Пользователь не найден.")
            return

        for b in user.get_borrowed_books():
            if b.get_title() == title:
                user.return_book(b)
                return
        print(f"У пользователя {user_name} нет такой книги")


if __name__ == '__main__':
    lib = Library()

    # --- создаём книги ---
    b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
    b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
    b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480, "плохая")

    # --- создаём пользователей ---
    user1 = User("Анна")
    librarian = Librarian("Мария")

    # --- библиотекарь добавляет книги ---
    librarian.add_book(lib, b1)
    librarian.add_book(lib, b2)
    librarian.add_book(lib, b3)

    # --- библиотекарь регистрирует пользователя ---
    librarian.register_user(lib, user1)

    # --- пользователь берёт книгу ---
    lib.lend_book("Война и мир", "Анна")

    # --- пользователь смотрит свои книги ---
    user1.show_books()

    # --- возвращает книгу ---
    lib.return_book("Война и мир", "Анна")

    # --- электронная книга ---
    b2.download()

    # --- ремонт книги ---
    b3.repair()
    print(b3)
