from zipfile import ZipFile
import frame, os, requests, sqlite3
from threading import Thread
from config import *



def on_start(): #TODO refactor this pls to try/catch
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
            r = requests.get(v_url) 
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
        desc = cursor.fetchall()
        frame.text_description.replace('1.0', 'end', desc[index][0])
        connection.close()
    except Exception as e:
        print(e, '(read description)')


def read_url(index):
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()
        cursor.execute('SELECT url FROM versions')
        url = str(cursor.fetchall()[index][0])
        connection.close()
        return url
    except Exception as e:
        print(e, '(read url)')


def check_version(index, state):
    if os.path.exists(str(os.getenv('APPDATA')) + '\\.minecraft\\versions') == False:
        os.mkdir(str(os.getenv('APPDATA')) + '\\.minecraft\\versions')
    if os.path.exists(str(os.getenv('APPDATA')) + '\\.minecraft\\versions\\' + names[index][0]) and state==False:
        return True
    else: 
        return False


def update_version():
    frame.progressbar.place(x=x_r, y=235, width=145, height=19)
    index = frame.listbox_versions.curselection()[0]
    with open(v_path + names[index][0] + '.zip', 'wb') as f:
        response = requests.get(f'https://www.dropbox.com/s/{read_url(index)}/{names[index][0]}.zip?dl=1', stream=True)
        total_length = response.headers.get('content-length')
        if total_length is None:
            f.write(response.content)
            return False
        else:           
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=int(total_length/100)):
                f.write(data)
                frame.progressbar['value'] += 1
            frame.progressbar.place_forget()
    with ZipFile(v_path + names[index][0] + '.zip', 'r') as z:
        z.extractall(path=v_path)
    os.remove(v_path + names[index][0] + '.zip') #TODO export to config current path


def button_work_click():
    thread_update = Thread(target=update_version)
    try:
        thread_update.start()
    except Exception as e:
        print(e, '(thread_update) start thread false')


def menu_settings_click():
    os.startfile(str(os.getenv('APPDATA')) + '\\.minecraft\\TLauncher.exe')
    print('launcher')


def listbox_versions_click(event):
    frame.button_work['text'] = 'Choose'
    frame.button_work['state'] = ['active']
    try:
        index = frame.listbox_versions.curselection()[0]
        read_description(index)
        frame.button_work['text'] = 'Update' if check_version(index, False) else 'Download'
    except Exception as e:
        frame.button_work['state'] = ['disabled']
        print(e, '(version click) its normal work')