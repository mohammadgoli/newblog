__author__ = 'root'
from views import db
from _config import DATABASE_PATH
import sqlite3

with sqlite3.connect(DATABASE_PATH) as connection:
    c = connection.cursor()
    c.execute("""ALTER TABLE blogposts RENAME TO old_posts""")
    db.create_all()
    c.execute("""SELECT header, body FROM old_posts""")
    data = [('text', row[0], 'this is a test post', row[1]) for row in c.fetchall()]

    c.executemany("""INSERT INTO blogposts (subject, header, digest, body) VALUES (?, ?, ?, ?)""", data)
    c.execute("""DROP TABLE old_posts""")

    c.execute("""ALTER TABLE comments RENAME TO old_comments""")
    db.create_all()
    c.execute("""SELECT name, email, comment FROM old_comments""")
    data = [(row[0], row[1], row[2], 0) for row in c.fetchall()]

    c.executemany("""INSERT INTO comments (name, email, comment, post_id) VALUES (?, ?, ?, ?)""", data)
    c.execute("""DROP TABLE old_comments""")
