import sys
import webbrowser
import db_handler

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("noneuser_menu.ui", self)
        self.login_but.clicked.connect(lambda: toNext(LoginWindow))

        self.dictionary.clicked.connect(lambda: toNext(BaseDictionary))

        self.vk_link.clicked.connect(lambda: webbrowser.open('#'))
        self.github_link.clicked.connect(
            lambda: webbrowser.open('https://github.com/samotny-vouk/PyQT-Project-2024-1courseFEFU-'))
        self.telegram_link.clicked.connect(lambda: webbrowser.open('https://t.me/+QUVnH3rO-D80ZWYy'))


class MainLogged(QMainWindow):
    def __init__(self):
        super(MainLogged, self).__init__()
        loadUi("adv_user_menu.ui", self)
        self.login_but.clicked.connect(lambda: toNext(LoginWindow))
        self.login_but.setText()
        self.dictionary_adv.clicked.connect(lambda: toNext(AdvDictionary))

        self.vk_link.clicked.connect(lambda: webbrowser.open('#'))
        self.github_link.clicked.connect(
            lambda: webbrowser.open('https://github.com/samotny-vouk/PyQT-Project-2024-1courseFEFU-'))
        self.telegram_link.clicked.connect(lambda: webbrowser.open('https://t.me/+QUVnH3rO-D80ZWYy'))


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("login_window.ui", self)

        name_or_mail = self.email_login.text()
        password = self.password_login.text()
        is_logged = db_handler.login(name_or_mail, password)
        if is_logged:
            self.login_try.clicked.connect(lambda: toNext(MainLogged))
        else:
            self.login_try.clicked.connect(lambda: toNext(RegisterWindow))

        self.to_register.clicked.connect(self.goToRegister)
        self.back.clicked.connect(lambda: toBack())

    def goToRegister(self):
        registerWindow = RegisterWindow()
        widget.addWidget(registerWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        loadUi("register_window.ui", self)
        self.back.clicked.connect(lambda: toBack())


class BaseDictionary(QMainWindow):
    def __init__(self):
        super(BaseDictionary, self).__init__()
        loadUi("dictionary_noneuser.ui", self)
        #self.to_add_word.clicked.connect(self.goToAddingWords)
        self.back.clicked.connect(lambda: toBack())
        # self.back1.clicked.connect(self.gotoMainWindow)


class AdvDictionary(QMainWindow):
    def __init__(self):
        super(AdvDictionary, self).__init__()
        loadUi("dictionary_advanced.ui", self)
        self.to_add_word.clicked.connect(self.goToAddingWords)
        self.back.clicked.connect(lambda: toBack())
        # self.back1.clicked.connect(self.gotoMainWindow)

    def goToAddingWords(self):
        adding_words = AddingWords()
        widget.addWidget(adding_words)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class AddingWords(QMainWindow):
    def __init__(self):
        super(AddingWords, self).__init__()
        loadUi("adding_new_word.ui", self)
        self.back.clicked.connect(lambda: toBack())
        # self.pushButton.clicked.connect(self.gotowindow2)


def toNext(WindowNext):
    windowNext = WindowNext()
    widget.addWidget(windowNext)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def toBack():
    if widget.count() > 1:
        widget.setCurrentIndex(widget.currentIndex() - 1)
        widget.removeWidget(widget.widget(widget.currentIndex() + 1))


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow1 = MainWindow()
widget.addWidget(mainwindow1)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
