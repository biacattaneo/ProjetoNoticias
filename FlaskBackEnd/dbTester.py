import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
#cursor.execute("DROP TABLE usuario")
conn.commit();