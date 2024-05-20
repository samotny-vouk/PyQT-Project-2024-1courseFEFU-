import sys
import webbrowser

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("noneuser_menu.ui", self)
        self.login_but.clicked.connect(lambda: toNext(LoginWindow))

        self.dictionary.clicked.connect(lambda: toNext(AdvDictionary))

        self.vk_link.clicked.connect(lambda: webbrowser.open('#'))
        self.github_link.clicked.connect(
            lambda: webbrowser.open('https://github.com/samotny-vouk/PyQT-Project-2024-1courseFEFU-'))
        self.telegram_link.clicked.connect(lambda: webbrowser.open('https://t.me/+QUVnH3rO-D80ZWYy'))


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("login_window.ui", self)

        self.pushButton.clicked.connect(self.goToRegister)
        self.back.clicked.connect(lambda: toBack())

    def gotoWindow(self):
        # mainWindow = MainWindow()
        # widget.addWidget(mainWindow)
        # widget.setCurrentIndex(widget.currentIndex() + 1)
        # print(widget.size())
        pass


    def goToRegister(self):
        registerWindow = RegisterWindow()
        widget.addWidget(registerWindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # def goToAddingWords(self):
    #     addingWords = AddingWords()
    #     widget.addWidget(addingWords)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)


class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        loadUi("register_window.ui", self)
        self.back.clicked.connect(lambda: toBack())
        #self.pushButton.clicked.connect(self.gotowindow2)

    # def gotowindow2(self):
    #     screen2 = SecondWindow()
    #     widget.addWidget(screen2)
    #     widget.setCurrentIndex(widget.currentIndex() + 1)


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
    # windowBack = WindowBack()
    widget.setCurrentIndex(widget.currentIndex() - 1)
    # widget.widgetRemoved(widget.currentIndex()+1)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow1 = MainWindow()
widget.addWidget(mainwindow1)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
