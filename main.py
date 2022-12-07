import onscreen
from kivy.app import App

class MyApp(App):

    def build(self):
        return onscreen.LoginScreen()


if __name__ == '__main__':
    MyApp().run()