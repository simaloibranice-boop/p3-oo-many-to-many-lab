from __future__ import annotations
from typing import List
from datetime import date

class Author:
    all_authors: List[Author] = []

    def __init__(self, name: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        self.name = name
        Author.all_authors.append(self)

    @property
    def contracts(self) -> List[Contract]:
        return [contract for contract in Contract.all_contracts if contract.author is self]

    @property
    def books(self) -> List[Book]:
        return [contract.book for contract in self.contracts]

    def sign_contract(self, book: Book, date_: date, royalties: float) -> Contract:
        return Contract(self, book, date_, royalties)

    @property
    def total_royalties(self) -> float:
        return sum(contract.royalties for contract in self.contracts)

    def __repr__(self) -> str:
        return f"<Author: {self.name}>"

class Book:
    all_books: List[Book] = []

    def __init__(self, title: str) -> None:
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title must be a non-empty string")
        self.title = title
        Book.all_books.append(self)

    def __repr__(self) -> str:
        return f"<Book: {self.title}>"

class Contract:
    all_contracts: List[Contract] = []

    def __init__(self, author: Author, book: Book, date_: date, royalties: float) -> None:
        if not isinstance(author, Author):
            raise ValueError("author must be an Author object")
        if not isinstance(book, Book):
            raise ValueError("book must be a Book object")
        if not isinstance(date_, date):
            raise ValueError("date must be a datetime.date object")
        if not isinstance(royalties, (int, float)) or royalties < 0:
            raise ValueError("royalties must be a non-negative number")

        self.author = author
        self.book = book
        self.date = date_
        self.royalties = float(royalties)
        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date_: date) -> List[Contract]:
        return [contract for contract in cls.all_contracts if contract.date == date_]

    def __repr__(self) -> str:
        return f"<Contract: {self.author.name} -> {self.book.title}, {self.royalties}%>"
