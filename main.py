from os import abort
import dearpygui.dearpygui as dpg
import modules.get_versions as get
import modules.dark_theme as dark_theme

def init():
    dpg.create_context()

    dark_theme.create_theme_dark()
    dark_theme.create_font()

    def onclick_quit():
        abort()

    def onclick_install():
        get.pack(get.versions()[0].index(dpg.get_value("listbox")))

    def onclick_choose_item(sender, app_data, user_data):#работает только так
        dpg.set_value(item="description", value=get.versions()[2][(get.versions()[0].index(app_data))])
        #при вызове функции описание выбирается поиском app_data из списка name,
        #с возвращением индекса совпадения, индекс указывает номер описания в списке description

    with dpg.window(tag="main"):
        vw, vh = 800, 290
        dpg.add_text("Welcome to Myne Loader for Minecraft")
        dpg.add_button(label="Exit", callback=onclick_quit, pos=[vw-70,vh-65])
        dpg.add_button(label="Install", callback=onclick_install, pos=[vw-170,vh-65])
        dpg.add_listbox(width=300, num_items=7, items=get.versions()[0], callback=onclick_choose_item, tag="listbox")
        dpg.add_text(default_value=get.versions()[2][0], wrap=vw-350, pos=[320,40], tag="description")
        dpg.add_input_text(pos=[8,vh-65], width=vw-187, tag="path")

    dpg.create_viewport(title='Myne', width=vw, height=vh, resizable=False, large_icon="assets/myne.ico")
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("main", True)
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == "__main__":
    init()