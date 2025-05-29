from  .connection import get_connection

def create_tables():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS directors(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT)
                   ''')
    cursor.execute('''

                   CREATE TABLE IF NOT EXISTS actors(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT)
                   ''')
    cursor.execute('''

                   CREATE TABLE IF NOT EXISTS Chief_crew(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   category TEXT
                   )''')
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS movies(
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   genre Text NOT NULL,
                   director_id INTEGER NOT NULL,
                   chief_crew_id INTEGER NOT NULL,
                   actors_id INTEGER NOT NULL,
                   FOREIGN KEY(actors_id) REFERENCES actors(id),
                   FOREIGN KEY(director_id) REFERENCES directors(id),
                   FOREIGN KEY(chief_crew_id) REFERENCES Chief_crew(id)
                   )
                   ''')
    conn.commit()
    conn.close()