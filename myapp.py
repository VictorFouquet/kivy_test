
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

    def get_devices_list():
        # Implement adb method
        pass
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

sm.current = "login"


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