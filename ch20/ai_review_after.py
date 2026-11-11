import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE records (day INTEGER, subject TEXT, hours REAL)")
conn.executemany("INSERT INTO records VALUES (?, ?, ?)", [
    (1, "파이썬", 1.5), (2, "통계학", 1.0), (3, "글쓰기", 0.5),
])


def find_by_subject(conn, subject):
    query = "SELECT day, hours FROM records WHERE subject = ?"
    return conn.execute(query, (subject,)).fetchall()   # 값은 따로 넘긴다


print(find_by_subject(conn, "파이썬"))
print(find_by_subject(conn, "없는과목' OR '1'='1"))
