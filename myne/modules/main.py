import frame, os, requests, sqlite3
from config import *


def on_start():
    if update_database()!=True:
        print(update_database())
    else:
        if read_name()==False:
            print('Database Error')


def update_database():
    if os.path.exists(db):
        return True
    else:
        try:
            r = requests.get(version_id_url) 
            f = open(db, 'wb') 
            f.write(r.content)
            return True
        except Exception as e:
            return e


def read_name():
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT name FROM versions')
        r = cursor.fetchall()
        for name in r:
            names.append(name)
            frame.listbox_versions.insert('end', name[0])
        connection.close()
        return True
    except Exception as e:
        print(e)
        return False


def read_description(index):
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT description FROM versions')
        r = cursor.fetchall()
        frame.text_description.replace('1.0', 'end', r[index][0])
        connection.close()
    except Exception as e:
        print(e)


def check_version(index):
    if os.path.exists('myne\\minecraft') == False:
        os.mkdir('myne\\minecraft')
    if os.path.exists('myne\\minecraft\\' + names[index][0]):
        return True
    else: 
        return False


def update_version():
    pass


def button_work_click():
    pass


def menu_settings_click():
	print('settings')


def listbox_versions_click(event):
    frame.button_work['text'] = 'Choose'
    frame.button_work['state'] = ['active']
    try:
        index = frame.listbox_versions.curselection()[0]
        read_description(index)
        frame.button_work['text'] = 'Play' if check_version(index) else 'Download'
    except Exception:
        frame.button_work['state'] = ['disabled']