class Book:
    def __init__(self, title, author, isbn, available):
        self.title: str = title
        self.author: str = author
        self.isbn: int = isbn
        self.available: bool = available
    
    def __str__(self):
        return f"{self.title}"
    
    def mark_as_borrower(self, member):
        pass

