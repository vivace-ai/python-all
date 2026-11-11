from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    pages: int


books = [
    Book("데이터 읽기", "김하늘", 2021, 320),
    Book("처음 만나는 통계", "박시우", 2019, 280),
    Book("일하는 사람의 글쓰기", "이도윤", 2023, 196),
]

for book in sorted(books, key=lambda b: b.year):
    print(book.year, book.title)

thick = [book.title for book in books if book.pages >= 250]
print(thick)
print(books[0] == Book("데이터 읽기", "김하늘", 2021, 320))
