import sqlite3
conn = sqlite3.connect("final.db")

print("Database connected.")

cmd = "CREATE TABLE final (name TEXT, checkin DATE, checkout DATE, roomtype TEXT)"

conn.execute(cmd)

print("Table created successfully")

conn.close()