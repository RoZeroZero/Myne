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
        desc = cursor.fetchall()
        frame.text_description.replace('1.0', 'end', desc[index][0])
        connection.close()
    except Exception as e:
        print(e, ',read description')


def check_version(index, state):
    if os.path.exists('myne\\minecraft') == False:
        os.mkdir('myne\\minecraft')
    if os.path.exists('myne\\minecraft\\' + names[index][0]) and state==False:
        return True
    else: 
        return False


def update_version():
    index = frame.listbox_versions.curselection()[0]
    with open('myne\\minecraft\\' + names[index][0] + '.zip', 'wb') as f:
        response = requests.get(version_id_url, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
            return False
        else:
            frame.progressbar.place(x=x_r, y=235, width=145, height=19)
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=int(total_length/100)):
                dl += len(data)
                f.write(data)
                frame.progressbar['value'] = int(100 * dl / total_length)
            frame.progressbar.place_forget()
            return True


def button_work_click():
    update_version()


def menu_settings_click():
	print('settings')


def listbox_versions_click(event):
    frame.button_work['text'] = 'Choose'
    frame.button_work['state'] = ['active']
    try:
        index = frame.listbox_versions.curselection()[0]
        read_description(index)
        frame.button_work['text'] = 'Play' if check_version(index, False) else 'Download'
    except Exception as e:
        frame.button_work['state'] = ['disabled']
        print(e, ',version click, its normal work')