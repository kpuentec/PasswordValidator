import bcrypt
import sqlite3
from datetime import datetime

def initialize_db():
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS passwords (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        hashed_password BLOB NOT NULL,
                        stored_at TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def hash(password):
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect("storage.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (hashed_password, stored_at) VALUES (?, ?)",
                    (hashed_pass, timestamp))
    conn.commit()
    conn.close()

    print("Password stored.")

if __name__ == "__main__":
    password = input("Enter your password: ")
    password_data = hash(password)
