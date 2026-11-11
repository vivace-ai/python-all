import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE records (day INTEGER, subject TEXT, hours REAL)")
conn.executemany("INSERT INTO records VALUES (?, ?, ?)", [
    (1, "파이썬", 1.5), (2, "통계학", 1.0), (3, "글쓰기", 0.5),
])


# AI가 내놓은 코드: 과목 이름으로 기록을 찾는다
def find_by_subject(conn, subject):
    query = f"SELECT day, hours FROM records WHERE subject = '{subject}'"
    return conn.execute(query).fetchall()


print(find_by_subject(conn, "파이썬"))
print(find_by_subject(conn, "없는과목' OR '1'='1"))
