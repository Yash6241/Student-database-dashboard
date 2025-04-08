import sqlite3

# Connect to SQLite database (it will create one if not exists)
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Drop table if exists (optional during dev)
cursor.execute("DROP TABLE IF EXISTS STUDENT")

# Create STUDENT table
cursor.execute("""
CREATE TABLE STUDENT (
    NAME TEXT,
    CLASS TEXT,
    SECTION TEXT,
    MARKS INTEGER
)
""")

# Insert sample data
students = [
    ("Alice", "Data Science", "A", 85),
    ("Bob", "Computer Science", "B", 76),
    ("Charlie", "Data Science", "A", 92),
    ("David", "Mathematics", "C", 67),
    ("Eva", "Data Science", "B", 88),
    ("Frank", "Computer Science", "A", 59)
]

cursor.executemany("INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)", students)

# Commit and close
conn.commit()
conn.close()

print("✅ student.db created and populated successfully!")
