class Author:
    all_authors = []  # class variable to track all authors

    def __init__(self, name):
        if not isinstance(name, str) or name.strip() == "":
            raise Exception("Name must be a non-empty string")
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        # return all Contract objects where this author is involved
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        # return all books this author has contracts for
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # create a new Contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # sum of royalties from all contracts
        return sum(contract.royalties for contract in self.contracts())

    def __repr__(self):
        return f"<Author: {self.name}>"




class Book:
    all_books = []  # class variable to track all books

    def __init__(self, title):
        if not isinstance(title, str) or title.strip() == "":
            raise Exception("Title must be a non-empty string")
        self.title = title
        Book.all_books.append(self)

    def __repr__(self):
        return f"<Book: {self.title}>"
 


class Contract:
    all_contracts = []  # track all contracts

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author object")
        if not isinstance(book, Book):
            raise Exception("book must be a Book object")
        if not isinstance(date, str) or date.strip() == "":
            raise Exception("date must be a non-empty string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("royalties must be a non-negative integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]

    def __repr__(self):
        return f"<Contract: {self.author.name} -> {self.book.title}, {self.royalties}%>"
