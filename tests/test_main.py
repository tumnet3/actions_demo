from src.library.library import book, PrintedBook, EBook, User, Library


def test_book_basic():
    b = book("Title", "Author", 2000)
    assert b.get_title() == "Title"
    assert b.get_author() == "Author"
    assert b.get_year() == 2000
    assert b.is_available() is True

    b.mark_as_taken()
    assert b.is_available() is False

    b.mark_as_returned()
    assert b.is_available() is True


def test_printed_book_repair():
    pb = PrintedBook("A", "B", 1990, 100, "плохая")
    pb.repair()
    assert pb.condition == "хорошая"


def test_ebook_properties():
    eb = EBook("E", "F", 2022, 5, "pdf")
    assert eb.file_size == 5
    assert eb.format == "pdf"


def test_user_borrow_and_return():
    u = User("Анна")
    b = book("X", "Y", 2001)

    u.borrow(b)
    assert b.is_available() is False
    assert b in u.get_borrowed_books()

    u.return_book(b)
    assert b.is_available() is True
    assert b not in u.get_borrowed_books()


def test_library_add_and_find():
    lib = Library()
    b = book("Book1", "Auth", 2020)
    lib.add_book(b)

    found = lib.find_book("Book1")
    assert found is b

    not_found = lib.find_book("Unknown")
    assert not_found is None
