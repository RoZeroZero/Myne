import dearpygui.dearpygui as dpg
import dark_theme

vw = 800
vh = 300

dpg.create_context()
dpg.bind_theme(dark_theme.create_theme_dark())
dpg.bind_font(dark_theme.create_font())

def button_callback():
    dpg.destroy_context()

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Exit", callback=button_callback, pos=[0.925*vw,0.9*vh])
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.create_viewport(title='Myne', width=vw, height=vh, resizable=False, decorated=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()