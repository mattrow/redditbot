import sqlite3

conn = sqlite3.connect('conversations.db')
cursor = conn.cursor()

# Create table to store conversation data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversations (
        user TEXT PRIMARY KEY,
        thread_id TEXT,
        last_message TEXT
    )
''')
conn.commit() 