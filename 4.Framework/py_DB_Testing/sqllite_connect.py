import sqlite3

# Connect to the in-memory database
conn = sqlite3.connect(':memory:')

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')

# Insert some data
cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
cursor.execute("INSERT INTO users (name) VALUES ('Bob')")

# Commit the changes
conn.commit()

# Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)

# The database connection will automatically close when the script ends,
# but you can also explicitly close it:
# conn.close()