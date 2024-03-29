import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306
    )

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Create Database
query_create = "CREATE DATABASE web_scrapping"
cur.execute(query_create)
cur.execute("USE web_scrapping")
cur.execute("CREATE TABLE news (id INT AUTO_INCREMENT, url TEXT, title TEXT,  PRIMARY KEY(id))")
cur.execute("INSERT INTO news (url, title) VALUES (?,?)", ("a","b"))

conn.commit() 
conn.close()
