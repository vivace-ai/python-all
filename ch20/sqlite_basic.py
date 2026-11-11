import sqlite3

conn = sqlite3.connect(":memory:")  # 메모리에만 있는 데이터베이스

conn.execute("""
    CREATE TABLE records (
        id      INTEGER PRIMARY KEY,
        day     INTEGER NOT NULL,
        subject TEXT    NOT NULL,
        hours   REAL    NOT NULL
    )
""")

rows = [(1, "파이썬", 1.5), (2, "통계학", 1.0), (3, "파이썬", 2.0)]
conn.executemany(
    "INSERT INTO records (day, subject, hours) VALUES (?, ?, ?)", rows
)
conn.commit()                       # 바꾼 내용을 확정한다

for row in conn.execute("SELECT id, day, subject, hours FROM records"):
    print(row)

conn.close()
