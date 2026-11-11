import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
conn.execute("""
    CREATE TABLE books (
        id    INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        year  INTEGER,
        done  INTEGER DEFAULT 0
    )
""")
books = [
    ("데이터 읽기", 2021),
    ("처음 만나는 통계", 2019),
    ("일하는 사람의 글쓰기", 2023),
]
conn.executemany("INSERT INTO books (title, year) VALUES (?, ?)", books)

conn.execute("UPDATE books SET done = 1 WHERE title = ?", ("데이터 읽기",))
conn.execute("DELETE FROM books WHERE year < ?", (2020,))

query = "SELECT id, title, year, done FROM books ORDER BY year"
for row in conn.execute(query):
    state = "읽음" if row["done"] else "읽는 중"
    print(row["id"], row["title"], row["year"], state)
