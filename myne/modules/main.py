import frame, tkinter
import versions

if __name__ == '__main__':
    frame()

def button_work_click(event):
        frame.listbox_versions.insert(0, versions.get.update([0]))

def menu_settings_click():
        print("settings")
