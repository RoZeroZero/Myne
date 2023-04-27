import sqlite3

with sqlite3.connect('versions.db') as db:
    cursor = db.cursor()
    cursor.execute(""" DROP TABLE IF EXISTS versions """)

    # создаем первую таблицу
    cursor.execute(""" CREATE TABLE IF NOT EXISTS versions (id INTEGER PRIMARY KEY, name TEXT, version INTEGER, description TEXT, url TEXT) """)
    cursor.executescript("""

    INSERT INTO versions(name, version, description, url) VALUES('Cosmo 1.12.2', 1, 'Земля обернулась безжизненной пустыней, вероятно, Вы одни из тех, кому предстоит ее возродить. Вам предстоит находить жизнь в мёртвой почве, чтобы найти пропитание и в конечном итоге познать космические технологии, чтобы исследовать новые планеты.', '2my8gi447rd10pg');
    INSERT INTO versions(name, version, description, url) VALUES('ReCreated 1.16.5', 1, 'Расширенное приключение в майнкрафт с модом Create.', 'i2d4cymdin2l4xq');
    INSERT INTO versions(name, version, description, url) VALUES('PrettyAdventure 1.19', 1, 'Добро пожаловать в мир открытый, изучайте самые дальние уголки природы и ищите самые красивые ландшафты!', 'ezl01vve6wwo1kz');
    INSERT INTO versions(name, version, description, url) VALUES('Build 1.12.2', 1, 'Все что нужно для создания построек и подготовки карт.', 'i2wbs3iejbqg5yr');
    INSERT INTO versions(name, version, description, url) VALUES('StayAlive 1.16.5', 1, 'Умри достойно! Избегай толп зомби, изучай заброшенные города и отстраивай самую защищенную базу.', 'f8uc28flr8sshur');""")

    db.commit()