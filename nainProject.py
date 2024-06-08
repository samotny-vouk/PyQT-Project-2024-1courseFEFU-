import sys
import webbrowser
from check_db import *
import db_handler1

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
# from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("noneuser_menu.ui", self)

        self.start_but.clicked.connect(lambda: toNext(StartWindow))
        self.login_but.clicked.connect(lambda: toNext(LoginWindow))
        self.dictionary.clicked.connect(lambda: toNext(BaseDictionary))
        self.flashcards.clicked.connect(lambda: toNext(CardsWindow))
        self.settings.clicked.connect(lambda: toNext(SetWindow))

        self.vk_link.clicked.connect(lambda: webbrowser.open('#'))
        self.github_link.clicked.connect(
            lambda: webbrowser.open('https://github.com/samotny-vouk/PyQT-Project-2024-1courseFEFU-'))
        self.telegram_link.clicked.connect(lambda: webbrowser.open('https://t.me/+QUVnH3rO-D80ZWYy'))
        self.ask_autors.clicked.connect(
            lambda: webbrowser.open('https://www.riverbankcomputing.com/static/Docs/PyQt5/'))


class MainLogged(QMainWindow):
    def __init__(self):
        super(MainLogged, self).__init__()
        loadUi("adv_user_menu.ui", self)
        self.start_but.clicked.connect(lambda: toNext(StartWindow))
        self.login_but.clicked.connect(lambda: toNext(LoginWindow))
        self.dictionary_adv.clicked.connect(lambda: toNext(AdvDictionary))
        self.flashcards_adv.clicked.connect(lambda: toNext(CardsWindow))
        self.settings.clicked.connect(lambda: toNext(SetWindow))

        self.vk_link.clicked.connect(lambda: webbrowser.open('#'))
        self.github_link.clicked.connect(
            lambda: webbrowser.open('https://github.com/samotny-vouk/PyQT-Project-2024-1courseFEFU-'))
        self.telegram_link.clicked.connect(lambda: webbrowser.open('https://t.me/+QUVnH3rO-D80ZWYy'))
        self.ask_autors.clicked.connect(lambda: webbrowser.open('https://www.riverbankcomputing.com/static/Docs/PyQt5/'))


class StartWindow(QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        loadUi("game_start.ui", self)

        self.back.clicked.connect(lambda: toBack())


class CardsWindow(QMainWindow):
    def __init__(self):
        super(CardsWindow, self).__init__()
        loadUi("game_start.ui", self)

        self.back.clicked.connect(lambda: toBack())


class SetWindow(QMainWindow):
    def __init__(self):
        super(SetWindow, self).__init__()
        loadUi("settings.ui", self)
        # self.dark_mode.clicked.connect(self.darkMode)
        # self.dark_mode.clicked.connect(lambda: self.savePrefs(0, "darkmode"))
        # self.light_mode.clicked.connect(self.lightMode)
        # self.light_mode.clicked.connect(lambda: self.savePrefs(0, "lightmode"))
        # self.inherit.setModal(True)
        # self.inherit.show()
        #
        # if str(QCoreApplication.instance().styleSheet()).find("color: rgb(255, 255, 255)") == 148:
        #     self.dark_mode.setChecked(True)
        # elif str(QCoreApplication.instance().styleSheet()).find("color: rgb(255, 255, 255)") == 8:
        #     self.light_mode.setChecked(True)
        # def darkMode(self):  # sets palette with dark values
        #     darkSettings = ("""* {
        # 		color: rgb(255, 255, 255);
        # 		background-color: rgb(25, 25, 25);
        # 		alternate-background-color: rgb(80, 80, 80);}
        # 		QRadioButton::indicator {
        # 		border: 1px solid rgb(255, 255, 255);
        # 		border-radius: 7px}
        # 		QRadioButton::indicator::checked {
        # 		background-color: rgb(255, 255, 255)}
        # 		QTabWidget * {
        # 		background-color: rgb(53, 53, 53)}
        # 		QTabWidget QScrollArea * {
        # 		background-color: rgb(25, 25, 25)}
        # 		QTabWidget QScrollArea QTableView {
        # 		background-color: rgb(53, 53, 53);
        # 		gridline-color: rgb(0, 0, 0)}
        # 		QTabWidget QScrollArea QHeader {
        # 		background-color: rgb(53, 53, 53)}
        # 		QTabWidget QScrollArea QScrollBar {
        # 		background-color: rgb(53, 53, 53)}
        # 		QLineEdit {
        # 		background-color: rgb(80, 80, 80)}
        # 		QCheckBox::indicator {
        # 		border: 1px solid rgb(255, 255, 255);
        # 		background: none;}
        # 		QCheckBox::indicator::checked {
        # 		background: rgb(255, 255, 255)}
        # 		QLCDNumber {
        # 		background-color: rgb(25, 25, 25)}
        # 		""")
        #     QCoreApplication.instance().setStyleSheet(f"* {darkSettings}")
        #
        # def lightMode(self):  # sets palette with light values
        #     lightSettings = ("""{
        # 		color: rgb(0, 0, 0);
        # 		background-color: rgb(211, 211, 211);
        # 		alternate-background-color: rgb(180, 180, 180);}
        # 		QTabWidget * {
        # 		background-color: rgb(255, 255, 255)}
        # 		QTabWidget QScrollArea * {
        # 		background-color: rgb(211, 211, 211)}
        # 		QTabWidget QScrollArea QTableView {
        # 		background-color: rgb(255, 255, 255);
        # 		gridline-color: rgb(0, 0, 0)}
        # 		QTabWidget QScrollArea QHeader {
        # 		background-color: rgb(255, 255, 255)}
        # 		QTabWidget QScrollArea QScrollBar {
        # 		background-color: rgb(255, 255, 255)}
        # 		QLineEdit {
        # 		background-color: rgb(180, 180, 180)}
        # 		QLCDNumber {
        # 		background-color: rgb(140,140,140)}
        # 		""")
        #     QCoreApplication.instance().setStyleSheet(f"* {lightSettings}")
        #
        # def savePrefs(self, mode, text):  # adds the new values to the preferences reference file
        #     values = []
        #     with open("preferences.csv", "r", newline="", encoding="utf-8") as preferences:
        #         values.append([row for row in csv.reader(preferences, delimiter=",")][0])
        #     preferences.close()
        #     if mode == 0:
        #         if text == "darkmode":
        #             values[0][0] = "darkmode"
        #         elif text == "lightmode":
        #             values[0][0] = "lightmode"
        #
        #     with open("preferences.csv", "w+", newline="", encoding="utf-8") as preferences:
        #         preferences.truncate()
        #         x = csv.writer(preferences)
        #         x.writerow(values[0])
        #     preferences.close()

        self.back.clicked.connect(lambda: toBack())


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("login_window.ui", self)
        # is_logged = True
        self.login_try.clicked.connect(self.auth)
        self.base_line_edit = [self.email_login, self.password_login]
        self.check_db = CheckThread()
        self.check_db.my_signal.connect(self.signal_handler)
        self.check_db.Boolean_signal.connect(self.boolean_signal)
        self.to_register.clicked.connect(lambda: toNext(RegisterWindow))
        self.back.clicked.connect(lambda: toBack())

    def check_intput(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)
        return wrapper

    def signal_handler(self, value):
        QMessageBox.about(self, "Notification", value)

    def boolean_signal(self, value):

        if value == True:
            toNext(MainLogged)
        else:
            toBack()

    @check_intput
    def auth(self):
        name = self.email_login.text()
        passw = self.password_login.text()
        self.check_db.thr_login(name, passw)


class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        loadUi("register_window.ui", self)
        # self.back.clicked.connect(lambda: toBack())
        self.register_new.clicked.connect(self.reg)
        self.base_line_edit = [self.username_new, self.email_new, self.password_new]
        self.check_db = CheckThread()
        self.check_db.Boolean_signal.connect(self.boolean_signal)
        self.check_db.my_signal.connect(self.signal_handler)
        self.back.clicked.connect(lambda: toBack())

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    def signal_handler(self, value):
        QMessageBox.about(self, "Notification", value)

    def boolean_signal(self, value):
        if value == True:
            toBack()
        else:
            toNext(MainLogged)

    @check_input
    def reg(self):
        name = self.username_new.text()
        mail = self.email_new.text()
        passw = self.password_new.text()
        self.check_db.thr_register(name, mail, passw)


class BaseDictionary(QMainWindow):
    def __init__(self):
        super(BaseDictionary, self).__init__()
        loadUi("dictionary_noneuser.ui", self)

        # self.params = {}

        #
        # self.comboBox = QtWidgets.QComboBox(self)
        # self.comboBox.setGeometry(QtCore.QRect(10, 10, 160, 20))
        # self.selectGenres()
        #
        self.search.clicked.connect(self.select)

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["WORDS TO LEARN"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)

        # self.to_add_word.clicked.connect(self.goToAddingWords)
        self.back.clicked.connect(lambda: toBack())
        # self.back1.clicked.connect(self.gotoMainWindow)

    # def selectGenres(self):
    #     req = "SELECT * from Words"
    #     cur1 = self.db.cursor()
    #     for category, wordID in cur1.execute(req).fetchall():
    #         self.params[wordID] = category
    #     self.comboBox.addItems(list(self.params.keys()))
    #
    def select(self):
        data = sqlite3.connect('project2024.db')
        cursor = data.cursor()
        result = cursor.execute(f'SELECT * FROM Words WHERE category == 1').fetchall()
        self.tableWidget.setRowCount(len(result))
        for i, row in enumerate(result):
            item = QTableWidgetItem(row[0])
            self.tableWidget.setItem(i, 0, item)
    #     req = "SELECT * FROM Words WHERE category = ?"
    #     category = self.params.get(self.comboBox.currentText())
    #     cur2 = self.db.cursor()
    #     result = cur2.execute(req, (category,)).fetchall()
    #


class AdvDictionary(QMainWindow):
    def __init__(self):
        super(AdvDictionary, self).__init__()
        loadUi("dictionary_advanced.ui", self)
        self.to_add_word.clicked.connect(lambda: toNext(AddingWords))
        self.to_change_word.clicked.connect(lambda: toNext(ChangingWords))
        self.back.clicked.connect(lambda: toBack())
        # self.back1.clicked.connect(self.gotoMainWindow)


class AddingWords(QMainWindow):
    def __init__(self):
        super(AddingWords, self).__init__()
        loadUi("adding_new_word.ui", self)

        self.add_word.clicked.connect(self.auth)
        self.back.clicked.connect(lambda: toBack())

    def auth(self):
        word = self.word_input.text()
        translate1 = self.translation1_input.text()
        translate2 = self.translation2_input.text()
        sentence = self.sentence_input.toPlainText()
        imgLink = self.image_link_input.text()
        s = self.is_subject.isChecked()
        a = self.is_adjective.isChecked()
        v = self.is_verb.isChecked()
        abbr = self.is_abbreviation.isChecked()

        sav = '0'
        if s:
            sav = '1'
        elif a:
            sav = '2'
        elif v:
            sav = '3'
        elif abbr:
            sav = '4'

        db_handler1.new_word(word, translate1, translate2, sav, sentence, imgLink)


class ChangingWords(QMainWindow):
    def __init__(self):
        super(ChangingWords, self).__init__()
        loadUi("changing_word.ui", self)

        self.change_word.clicked.connect(self.auth)
        self.back.clicked.connect(lambda: toBack())

    def auth(self):
        word = self.word_input.text()
        translate1 = self.translation1_input.text()
        translate2 = self.translation2_input.text()
        sentence = self.sentence_input.toPlainText()
        imgLink = self.image_link_input.text()
        s = self.is_subject.isChecked()
        a = self.is_adjective.isChecked()
        v = self.is_verb.isChecked()
        abbr = self.is_abbreviation.isChecked()

        sav = '0'
        if s:
            sav = '1'
        elif a:
            sav = '2'
        elif v:
            sav = '3'
        elif abbr:
            sav = '4'

        db_handler1.change_word(word, translate1, translate2, sav, sentence, imgLink)


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
main_window = MainWindow()
widget.addWidget(main_window)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
