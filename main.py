import dearpygui.dearpygui as dpg
# import dearpygui.demo as demo
import dark_theme

vw = 800
vh = 300

dpg.create_context()
dark_theme.create_theme_dark()
dark_theme.create_font()


def button_callback():
    exit()

with dpg.window(tag="Primary Window"):
    dpg.add_text("Myne")
    dpg.add_button(label="Exit", callback=button_callback, pos=[0.915*vw,0.79*vh])


dpg.create_viewport(title='Myne', width=vw, height=vh, resizable=False, decorated=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()