
import platform
import requests
import os

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from database import Database


class WindowManager(ScreenManager):
    pass


class P(FloatLayout):
    close_btn = ObjectProperty(None)


class MainWindow(Screen):
    conn_device = ObjectProperty(None)
    dl_os = ObjectProperty(None)

    def get_devices_list(self):
        # Implement adb method
        pass

    def download_os(self):
        # Replace with adb method
        path = os.getcwd()
        user_os = platform.system()

        dl_path = f"{path}/cache/pic1.jpg" if user_os == "Linux" else f"{path}\\cache\\pic1.jpg"

        with open(dl_path, 'wb') as handle:
                response = requests.get("https://live.staticflickr.com/7357/10471925145_60d4d52bb4_b.jpg", stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)

    '''
    usr_email = ObjectProperty(None)
    created = ObjectProperty(None)
    current = ""

    def log_out(self):
        sm.current = "login"

    def on_enter(self, *args):
        email, created = db.get_user(self.current)
        self.usr_email.text = "Account email : " + email
        self.created.text = "Created : " + created
    '''
    pass

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_btn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalid_login()
    
    def reset(self):
        self.email.text = ""
        self.password.text = ""


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = Database("users.txt")

screens = [LoginWindow(name="login"), MainWindow(name="main")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


def invalid_login():
    content = P()
    pop = Popup(title="Invalid Login",
        content=content,
        size_hint=(None, None), size=(350,350)
    )
    content.close_btn.bind(on_press=pop.dismiss)
    pop.open()

class MyApp(App):
    def build(self):
        return sm