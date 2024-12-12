import sqlite3
import userStore

def get_db_connection():
    conn = sqlite3.connect('userDB.db', timeout=10.0)
    conn.row_factory = sqlite3.Row
    return conn

def update_Weight(userName, weight):
    conn = get_db_connection()
    cur = conn.cursor()
    
    try:
        res = cur.execute("UPDATE users SET userWeight = ? WHERE userName = ?", (weight, userName))
        userStore.set_weight(weight)
        message = "Weight successfully updated"
        print(message)
    except sqlite3.Error as e:
        print(f"Database error: {e}")  # Prints the full error message

    conn.commit()
    cur.close()
    conn.close()   
    print("connection cleaned")

def get_Weight_from_db(userName):
    conn = get_db_connection()
    cur = conn.cursor()
    weight = 0

    try:
        res = cur.execute("SELECT userWeight FROM users WHERE userName = ?", (userName, ))
        result = cur.fetchone()
        weight = result[0]
        message = "Weight successfully retrieved"
        print(message)
    except sqlite3.Error as e:
        print(f"Database error: {e}")  # Prints the full error message

    conn.close()
    return weight

