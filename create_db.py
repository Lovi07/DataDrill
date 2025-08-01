import sqlite3

# Connect to new SQLite database file (creates it if not exists)
conn = sqlite3.connect("data/sample_sales.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    region TEXT,
    quantity INTEGER,
    revenue REAL,
    sale_date TEXT
)
""")

# Insert sample data
sales_data = [
    ('Apples', 'North', 100, 1200.0, '2023-01-01'),
    ('Bananas', 'South', 150, 900.0, '2023-01-02'),
    ('Apples', 'East', 200, 2400.0, '2023-01-03'),
    ('Oranges', 'West', 180, 1100.0, '2023-01-04')
]

cursor.executemany("""
INSERT INTO sales (product, region, quantity, revenue, sale_date)
VALUES (?, ?, ?, ?, ?)
""", sales_data)

conn.commit()
conn.close()

print("✅ Database created at: data/sample_sales.db")
