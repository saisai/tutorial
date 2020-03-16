import psycopg2

conn = psycopg2.connect(database="test",
                        user="testuser",
                         password="testuser",
                         host="127.0.0.1",
                         port=5432)
print(conn)
cur = conn.cursor()

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
    print("ID = ", row[0])
    print("Name = ", row[1])
    print("Address = ", row[2])
    print("Salary = ", row[3])
    
conn.close()
