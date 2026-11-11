import sqlite3

conn = sqlite3.connect(":memory:")
conn.row_factory = sqlite3.Row
conn.execute("CREATE TABLE orders (customer TEXT, item TEXT, amount INTEGER)")
conn.executemany("INSERT INTO orders VALUES (?, ?, ?)", [
    ("이서연", "키보드", 89000), ("박준호", "마우스", 35000),
    ("이서연", "모니터", 420000), ("최민지", "키보드", 89000),
    ("박준호", "키보드", 89000),
])

query = """
    SELECT customer, COUNT(*) AS n, SUM(amount) AS total
    FROM orders
    GROUP BY customer
    HAVING total >= ?
    ORDER BY total DESC
"""
for rank, row in enumerate(conn.execute(query, (100000,)), start=1):
    print(f"{rank}위 {row['customer']} {row['n']}건 {row['total']:,}원")
