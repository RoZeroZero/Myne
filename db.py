import sqlite3

with sqlite3.connect('versions.db') as db:
    cursor = db.cursor()
    cursor.execute(""" DROP TABLE IF EXISTS versions """)

    # создаем первую таблицу
    cursor.execute(""" CREATE TABLE IF NOT EXISTS versions (id INTEGER PRIMARY KEY, name TEXT, version INTEGER, description TEXT, url TEXT) """)
    cursor.executescript("""

    INSERT INTO versions(name, version, description, url) VALUES('Cosmo 1.12.2', 1, 'desc', '2my8gi447rd10pg');
    INSERT INTO versions(name, version, description, url) VALUES('ReCreated 1.16.5', 1, 'desc', 'i2d4cymdin2l4xq');
    INSERT INTO versions(name, version, description, url) VALUES('PrettyAdventure 1.19', 1, 'desc', 'ezl01vve6wwo1kz');
    INSERT INTO versions(name, version, description, url) VALUES('Build 1.12.2', 1, 'desc', 'i2wbs3iejbqg5yr');""")

    db.commit()