import sys
import webbrowser

import levels
from dbCheck import *
from qt_material import apply_stylesheet

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
# from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
dark_theme = False

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

        self.subjects.clicked.connect(lambda: webbrowser.open('https://en.wikipedia.org/wiki/Subject_(grammar)'))
        self.adjectives.clicked.connect(lambda: webbrowser.open('https://en.wikipedia.org/wiki/Adjective'))
        self.verbs.clicked.connect(lambda: webbrowser.open('https://en.wikipedia.org/wiki/Verb'))

        self.sub_1.clicked.connect(lambda: toNext(levels.level1_sub))
        self.sub_2.clicked.connect(lambda: toNext(levels.level2_sub))
        self.sub_3.clicked.connect(lambda: toNext(levels.level3_sub))
        self.sub_4.clicked.connect(lambda: toNext(levels.level4_sub))
        self.sub_5.clicked.connect(lambda: toNext(levels.level5_sub))

        self.adj_1.clicked.connect(lambda: toNext(levels.level1_adj))
        self.adj_2.clicked.connect(lambda: toNext(levels.level2_adj))
        self.adj_3.clicked.connect(lambda: toNext(levels.level3_adj))
        self.adj_4.clicked.connect(lambda: toNext(levels.level4_adj))
        self.adj_5.clicked.connect(lambda: toNext(levels.level5_adj))

        self.verb_1.clicked.connect(lambda: toNext(levels.level1_verb))
        self.verb_2.clicked.connect(lambda: toNext(levels.level2_verb))
        self.verb_3.clicked.connect(lambda: toNext(levels.level3_verb))
        self.verb_4.clicked.connect(lambda: toNext(levels.level4_verb))
        self.verb_5.clicked.connect(lambda: toNext(levels.level5_verb))

        self.back.clicked.connect(lambda: toBack())


class CardsWindow(QMainWindow):
    def __init__(self):
        super(CardsWindow, self).__init__()
        loadUi("flashcards.ui", self)

        self.btn_prev.setEnabled(False)
        self.btn_next.setEnabled(False)
        self.labshowbtn.hide()
        self.star_1.hide()
        self.star_0.clicked.connect(self.showStarChecked)
        self.star_1.clicked.connect(self.showStarNull)
        self.back.clicked.connect(lambda: toBack())

        if self.rb_know.isChecked() or self.rb_notknow.isChecked():
            self.btn_prev.setEnabled(True)
            self.btn_next.setEnabled(True)

        self.btn_show.clicked.connect(self.showMeaning)

    def showStarNull(self):
        self.star_1.hide()
        self.star_0.show()

    def showStarChecked(self):
        self.star_0.hide()
        self.star_1.show()

    def showMeaning(self):
        self.labshowbtn.show()
        self.btn_show.hide()


class SetWindow(QMainWindow):
    def __init__(self):
        super(SetWindow, self).__init__()
        loadUi("settings.ui", self)
        self.dark_mode.clicked.connect(self.darkMode)
        self.light_mode.clicked.connect(self.lightMode)

        self.back.clicked.connect(lambda: toBack())

    def darkMode(self):
        global dark_theme
        dark_theme = True

    def lightMode(self):
        global dark_theme
        dark_theme = False


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
        QMessageBox.about(self, "* * * * * * * * *", value)

    def boolean_signal(self, value):

        if value == True:
            toNext(MainLogged)
        else:
            toNext(RegisterWindow)

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
        QMessageBox.about(self, "* * * * * * * * *", value)

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

        self.check_db = CheckThread()
        self.check_db.Boolean_signal.connect(self.boolean_signal)
        self.check_db.my_signal.connect(self.signal_handler)
        self.add_word.clicked.connect(self.auth)
        self.back.clicked.connect(lambda: toBack())

    def signal_handler(self, value):
        QMessageBox.about(self, "* * * * * * * * *", value)

    def boolean_signal(self, value):
        if value == True:
            pass
        else:
            pass

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

        self.check_db.thr_new(word, translate1, translate2, sav, sentence, imgLink)


class ChangingWords(QMainWindow):
    def __init__(self):
        super(ChangingWords, self).__init__()
        loadUi("changing_word.ui", self)

        self.check_db = CheckThread()
        self.check_db.Boolean_signal.connect(self.boolean_signal)
        self.check_db.my_signal.connect(self.signal_handler)
        self.change_word.clicked.connect(self.auth)
        self.back.clicked.connect(lambda: toBack())

    def signal_handler(self, value):
        QMessageBox.about(self, "* * * * * * * * *", value)

    def boolean_signal(self, value):
        if value == True:
            pass
        else:
            pass

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

        self.check_db.thr_update(word, translate1, translate2, sav, sentence, imgLink)


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

if dark_theme:
    apply_stylesheet(app, theme='dark_teal.xml')

widget.addWidget(main_window)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
