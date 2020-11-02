from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
import re

Window.size = (360, 640)


class MainWindow(BoxLayout):
    def login(self):
        email = self.ids.login_email.text
        password = self.ids.login_password.text
        self.check_email(email)
        self.check_password(password)

    def check_password(self, password):
        if(password == ''):
            self.ids.login_label.text = 'ENTER PASSWORD'
        else:
            self.ids.login_label.text = ''

    def check_email(self, email):
        if re.match(r'[^@]+@[^@]+\.[^@]+', email) is None:
            self.ids.login_label.text = 'NOT A VALID EMAIL OR PASSWORD'
        else:
            self.ids.login_label.text = ''


class Geranda(App):
    def build(self):
        self.icon = 'UI/assets/Icon/Geranda.png'
        return MainWindow()


if __name__ == '__main__':
    Geranda().run()
