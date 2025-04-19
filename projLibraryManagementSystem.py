import pandas as pd
from datetime import datetime


class Book:
    def __init__(self,book_id, title, author, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def lend_copy(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print(f"Lent 1 copy of '{self.title}'. Remaining: {self.copies_available}")
        else:
            print(f"No copies available for '{self.title}'.")

    def return_copy(self):
        self.copies_available += 1 
        print(f"Returned 1 copy of '{self.title}'. Available now: {self.copies_available}")

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_id):
        if book_id not in self.borrowed_books:
            self.borrowed_books.append(book_id)
            print(self.borrowed_books)
            # print(f"{self.name} borrowed book ID: {book_id}")

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            print(f"{self.name} returned book ID: {book_id}")
        else:
            print(f"{self.name} does not have book ID: {book_id}")    

class Library:
    def __init__(self,library_name):
        self.library_name = library_name
        self.books = []
        self.members = []
        self.history = pd.DataFrame(columns=["DateTime", "MemberID", "MemberName", "BookID", "BookTitle", "Action"])
    
    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Book {book.title} with id {book.book_id} added successfully!")

    def add_member(self, member: Member):
        self.members.append(member)
        print(f"Member {member.name} with id {member.member_id} added successfully!")

    def find_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None
    def find_member_by_id(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def lend_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if member and book:
            if book.copies_available > 0:
                book.lend_copy()
                member.borrow_book(book_id)
                self._log_transaction(member, book, "Borrow")
            else:
                print("Sorry, book not available.")
        else:
            print("Invalid member ID or book ID.")


    def return_book(self, member_id, book_id):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_id(book_id)

        if member and book:
            book.return_copy()
            member.return_book(book_id)
            self._log_transaction(member, book, "Return")
        else:
            print("Invalid member ID or book ID.")




    def _log_transaction(self, member:Member, book:Book, action: str):
        new_log = {
            "DateTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "MemberID":member.member_id,
            "MemberName":member.name,
            "BookID": book.book_id,
            "BookTitle": book.title,
            "Action": action
        }
        self.history = pd.concat([self.history, pd.DataFrame([new_log])], ignore_index=True)

    def show_transaction_history(self):
        print("\n📚 Borrowing History:")
        print(self.history)

    def display_books(self):
        print(f"\nBooks in {self.library_name}:")
        for book in self.books:
            print(f"{book.book_id} | {book.title} | {book.author} | Available: {book.copies_available}")




# Create Books
book1 = Book(101, "Python Crash Course", "Eric Matthes", 3)
book2 = Book(102, "Atomic Habits", "James Clear", 2)
book3 = Book(103, "java Habits", "James Clear", 5)

# Create Members
member1 = Member(1, "Alice")
member2 = Member(2, "Bob")

# Create Library
lib = Library("Code Library")

# Add Books and Members
lib.add_book(book1)
lib.add_book(book2)
lib.add_book(book3)
lib.add_member(member1)
lib.add_member(member2)

# Lending and Returning Books
# lib.lend_book(1, 101)  # Alice borrows "Python Crash Course"
lib.lend_book(1, 103)  # Alice borrows "Python Crash Course"
lib.lend_book(2, 102)  # Bob borrows "Atomic Habits"
lib.return_book(1, 101)  # Alice returns her book

# Display current library status
lib.display_books()
# lib.show_transaction_history()


# book1 = Book(1, 'Physics', 'Faiz', 2)
# book2 = Book(2, 'Math', 'Faiz', 2)
# book3 = Book(3, 'Math', 'Faiz', 2)
# book4 = Book(4, 'Chemistry', 'Faiz', 2)
# book4 = Book(5, 'Biology', 'Tarana', 2)

# member1 = Member(1, 'Maaz')
# member2 = Member(2, 'Faiz')
# member3 = Member(3, 'Salman')
# member4 = Member(4, 'Masnoon')
# central_library = Library('Central Library')
# central_library.add_book(book1)
# central_library.add_member(member1)
