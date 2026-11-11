import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE records (day INTEGER, subject TEXT, hours REAL)")
conn.execute("SELECT day, hour FROM records")
