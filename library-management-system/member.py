class Member:
    def __init__(self, name, member_id, borrowed_books):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def __str__(self):
        return f"{self.name}: {self.borrowed_book}"