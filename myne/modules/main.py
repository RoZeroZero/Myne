import frame, tkinter, os, requests, sqlite3
from config import *


def on_start():
    check()
    if check()==False:
        print("Download Error")
    else:
        if read_name()==False:
            print("Database Error")


def check():
    if os.path.exists("versions.db"):
        return True
    else:
        update()
        return False


def update():
    r = requests.get(version_id_url) 
    with open('versions.db', 'wb') as f: 
        f.write(r.content)


def read_name():
    try:
        connection = sqlite3.connect('versions.db')
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM versions")
        r = cursor.fetchall()
        for name in r:
            frame.listbox_versions.insert(0, name[0])
        connection.close()
        return True
    except Exception as e:
        print(e)
        return False


def read_description():
    pass


def button_work_click(event):
	pass


def menu_settings_click():
	print("settings")