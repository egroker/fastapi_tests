import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT * FROM users")
result = cur.fetchall()
for row in result:
    print(row)
cur.close()
conn.close()