import dearpygui.dearpygui as dpg
import dark_theme

dpg.create_context()

dark_theme.create_theme_dark()
dark_theme.create_font()

def onclick_quit():
    quit()

def onclick_install():
    return

with dpg.window(tag="main"):
    vw, vh = 800, 290
    dpg.add_text("Welcome to Myne Loader for Minecraft")
    dpg.add_button(label="Exit", callback=onclick_quit, pos=[vw-70,vh-65])
    dpg.add_button(label="Install", callback=onclick_install, pos=[vw-170,vh-65])
    dpg.add_listbox(width=190, num_items=7)
    dpg.add_text("Description", wrap=vw-210, pos=[210,40])
    dpg.add_input_text(pos=[8,vh-65], width=vw-187)

dpg.create_viewport(title='Myne', width=vw, height=vh, resizable=False, large_icon="assets/myne.ico")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main", True)
dpg.start_dearpygui()
dpg.destroy_context()