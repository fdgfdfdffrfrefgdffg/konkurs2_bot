from sqlite3 import Connection

conn = Connection("data.db")
c = conn.cursor()

class User:
    def __init__(self, name, phone, status):
        self.name = name
        self.phone = phone
        self.status = status



def default_tasks():
    c.execute("CREATE TABLE IF NOT EXISTS users (id, name, phone, status)")
    c.execute("CREATE TABLE IF NOT EXISTS refs (user_id, reffer_id, status)")
    c.execute("CREATE TABLE IF NOT EXISTS channels (channel_id)")

    conn.commit()

def data_clear():
    c.execute("DELETE FROM users")
    c.execute("DELETE FROM refs")
    conn.commit()

def add_user(id, name, phone):
    c.execute("INSERT INTO users VALUES (?, ?, ?, 1)", (id, name, phone))
    conn.commit() 

def del_refs(user_id):
    c.execute("DELETE FROM refs WHERE user_id=? OR reffer_id=?", (user_id, user_id))
    conn.commit()

def get_user(id):
    data = c.execute("SELECT name, phone, status FROM users WHERE id=?", (id, )).fetchone()
    return User(data[0], data[1], data[2]) if data else None

def get_users():
    return c.execute("SELECT id, name, phone, status FROM users").fetchall()

def add_ref(user_id, reffer_id):
    c.execute("INSERT INTO refs VALUES (?, ?, 0)", (user_id, reffer_id))
    conn.commit()

def get_ref(user_id, reffer_id):
    return c.execute("SELECT user_id, reffer_id, status FROM refs WHERE user_id=? AND reffer_id=?", (user_id, reffer_id)).fetchone()

def get_reffer(user_id):
    return c.execute("SELECT user_id, reffer_id, status FROM refs WHERE user_id=?", (user_id, )).fetchone()


def get_stats():
    return c.execute("""
    SELECT reffer_id, COUNT(*) AS takrorlanish_soni
    FROM refs
    WHERE status = 1
    GROUP BY reffer_id
    ORDER BY takrorlanish_soni DESC;
    """).fetchall()

def get_ref_count(user_id):
    return c.execute(f"""
    SELECT reffer_id, COUNT(*) AS takrorlanish_soni
    FROM refs
    WHERE status = 1 AND reffer_id = {user_id}
    GROUP BY reffer_id
    ORDER BY takrorlanish_soni DESC;
    """).fetchall()

def get_refs():
    return c.execute("SELECT user_id, reffer_id, status FROM refs").fetchall()

def add_channel(id):
    c.execute("INSERT INTO channels VALUES (?)", (id, ))
    conn.commit()

def get_reffer_this_user(user_id):
    return c.execute("SELECT reffer_id FROM refs WHERE user_id=? OR reffer_id=?", (user_id, user_id)).fetchone()

def get_channel(id):
    return c.execute("SELECT channel_id FROM chhannels WHERE channel_id=?", (id, )).fetchone()

def get_channels():
    return c.execute("SELECT channel_id FROM channels").fetchall()

def del_channel(id):
    c.execute("DELETE FROM channels WHERE channel_id=?", (id, ))
    conn.commit()

def del_user(id):
    c.execute("DELETE FROM users WHERE id=?", (id, ))
    conn.commit()

def del_ref(user_id, reffer_id):
    c.execute("DELETE FROM refs WHERE user_id=? AND reffer_id=?", (user_id, reffer_id))
    conn.commit()

def change_status_user(id, status):
    c.execute("UPDATE users SET status=? WHERE id=?", (status, id))
    conn.commit()

def change_status_ref(user_id, status):
    c.execute("UPDATE refs SET status=? WHERE user_id=? OR reffer_id=?", (status, user_id, user_id))
    conn.commit()
