class Book:
    # Class variable to track all books
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        # Add this instance to the class-level tracking list
        Book.all_books.append(self)

    def contracts(self):
        """Return a list of contracts related to this book."""
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        """Return a list of authors related to this book through their contracts."""
        return [contract.author for contract in self.contracts()]


class Author:
    # Class variable to track all authors
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        # Add this instance to the class-level tracking list
        Author.all_authors.append(self)

    def contracts(self):
        """Return a list of contracts related to this author."""
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        """Return a list of books related to this author through their contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Sign a contract for a book with a specific date and royalty percentage."""
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        # Create and return a new contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the total royalties earned from all contracts."""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    # Class variable to track all contracts
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        # Add this instance to the class-level tracking list
        Contract.all_contracts.append(self)

    def __eq__(self, other):
        """Check equality based on author, book, date, and royalties."""
        if not isinstance(other, Contract):
            return False
        return (self.author == other.author and
                self.book == other.book and
                self.date == other.date and
                self.royalties == other.royalties)

    def __repr__(self):
        """Return a readable representation of the contract object."""
        return f"<Contract(author={self.author.name}, book={self.book.title}, date={self.date}, royalties={self.royalties})>"
    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts signed on a specific date."""
        return [contract for contract in cls.all_contracts if contract.date == date]

