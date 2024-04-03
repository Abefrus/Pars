import sqlite3

class CreateDb():
  conn = sqlite3.connect('data.db')
  cursor = conn.cursor()

  create_db = '''CREATE TABLE IF NOT EXISTS quotes (author TEXT, quote TEXT, tags TEXT)''' 

  cursor.execute(create_db)
  conn.commit()
  conn.close()