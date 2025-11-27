import sqlite3
db = 'db.sqlite3'
conn = sqlite3.connect(db)
cur = conn.cursor()
try:
    cur.execute("SELECT COUNT(*) FROM auth_user WHERE username = ?", ('admin',))
    admin_count = cur.fetchone()[0]
    print('auth_user admin count:', admin_count)
except Exception as e:
    print('auth_user query failed:', e)

try:
    cur.execute("SELECT id, title, description, resolved FROM myapp_todo")
    rows = cur.fetchall()
    print('myapp_todo rows:', len(rows))
    for r in rows:
        print(r)
except Exception as e:
    print('myapp_todo query failed:', e)
finally:
    conn.close()
