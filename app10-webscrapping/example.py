import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("app10-webscrapping/data.db")
cursor = connection.cursor()

# Query data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(type(rows))

cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

new_rows = [("Cats", "Cat City", "2088.10.17"),
            ("Hens", "Hens City", "2088.10.17")]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)