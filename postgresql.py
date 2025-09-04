import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="mydb",
    user="postgres",
    password="Tush@123",  # replace with your pgAdmin password
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
print("✅ Connected to Database")

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        designation VARCHAR(50),
        base_location VARCHAR(50)
    )
""")
conn.commit()
print("✅ Table created")

# Insert data
cursor.execute(
    "INSERT INTO employees (name, designation, base_location) VALUES (%s, %s, %s)",
    ("Tushar Verma", "Software Developer", "Noida")
)
cursor.execute(
    "INSERT INTO employees (name, designation, base_location) VALUES (%s, %s, %s)",
    ("Alice", "Data Analyst", "Pune")
)
conn.commit()
print("✅ Data inserted")

# Fetch data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

print("\n📌 Employee Records:")
for row in rows:
    print(row)

# Close connection
cursor.close()
conn.close()
print("✅ Connection closed")
