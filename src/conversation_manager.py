from src.database import conn, cursor

def user_has_been_contacted(username):
    cursor.execute('SELECT 1 FROM conversations WHERE user = ?', (username,))
    return cursor.fetchone() is not None

def save_conversation(username, reply_instance):
    cursor.execute(
        'INSERT INTO conversations (user, thread_id, last_message) VALUES (?, ?, ?)',
        (username, reply_instance.fullname, reply_instance.body)
    )
    conn.commit() 

def get_user_by_thread_id(thread_id):
    cursor.execute('SELECT user FROM conversations WHERE thread_id = ?', (thread_id,))
    result = cursor.fetchone()
    return result[0] if result else None

def get_full_conversation(message):
    conversation = []
    while message:
        conversation.append({
            'author': message.author.name,
            'body': message.body
        })
        if message.is_root:
            break
        message = message.parent()
    conversation.reverse()
    return conversation

def update_last_message(username, last_message):
    cursor.execute(
        'UPDATE conversations SET last_message = ? WHERE user = ?',
        (last_message, username)
    )
    conn.commit() 