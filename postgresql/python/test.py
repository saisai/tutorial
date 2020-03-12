import psycopg2

conn = psycopg2.connect(database="test",
                        user="testuser",
                         password="testuser",
                         host="127.0.0.1",
                         port=5432)
print(conn)
print(dir(conn))
