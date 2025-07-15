import sqlite3

conn = sqlite3.connect("site.db") 
cursor = conn.cursor()
cursor.execute('''
  create table users(
          id Integer Primary key AutoIncrement,
          name text not null ,
          email taxt unique not null )

 ''')
conn.commit()
conn.close()