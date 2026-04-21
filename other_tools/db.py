import mariadb

conn = mariadb.connect(
    user="user",
    password="password",
    host="localhost",
    port=3306,
    database="employees",
)

cur = conn.cursor()

cur.execute(
    "CREATE TABLE IF NOT EXISTS employees(id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100) NOT NULL)"
)
cur.execute("INSERT INTO employees(name) VALUES('John Doe')")
cur.execute("INSERT INTO employees(name) VALUES('Jane Doe')")
conn.commit()
