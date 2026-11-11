import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row  # 열 이름으로 값을 꺼낼 수 있게 한다
conn.execute("CREATE TABLE records (day INTEGER, subject TEXT, hours REAL)")
conn.executemany("INSERT INTO records VALUES (?, ?, ?)", [
    (1, "파이썬", 1.5), (2, "통계학", 1.0), (3, "파이썬", 2.0),
    (4, "글쓰기", 0.5), (5, "통계학", 2.0),
])

# 조건에 맞는 행을 골라 정렬한다
rows = conn.execute(
    "SELECT day, hours FROM records WHERE subject = ? ORDER BY hours DESC",
    ("파이썬",),
).fetchall()
print([(row["day"], row["hours"]) for row in rows])

# 과목별로 묶어 합계와 건수를 구한다
query = """
    SELECT subject, SUM(hours) AS total, COUNT(*) AS n
    FROM records GROUP BY subject ORDER BY total DESC
"""
for row in conn.execute(query):
    print(row["subject"], row["total"], row["n"])

# 고치고 지운다
conn.execute("UPDATE records SET hours = ? WHERE day = ?", (1.0, 4))
conn.execute("DELETE FROM records WHERE subject = ?", ("통계학",))
print(conn.execute("SELECT COUNT(*) FROM records").fetchone()[0])
