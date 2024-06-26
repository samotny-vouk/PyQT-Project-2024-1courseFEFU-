import os
import sys
import random
import webbrowser

import levels
from dbCheck import *
from qt_material import apply_stylesheet

from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
dark_theme = os.getenv("APP_THEME") == "dark"
try:
    f = open('text.txt', 'x')
    f.write('guest')
    f.close()
except:
    f = open('text.txt', 'w')
    f.write('guest')
    f.close()

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
        self.sub_2.clicked.connect(lambda: toNext(levels.level1_sub))
        self.sub_3.clicked.connect(lambda: toNext(levels.level1_sub))
        self.sub_4.clicked.connect(lambda: toNext(levels.level1_sub))
        self.sub_5.clicked.connect(lambda: toNext(levels.level1_sub))

        self.adj_1.clicked.connect(lambda: toNext(levels.level1_adj))
        self.adj_2.clicked.connect(lambda: toNext(levels.level1_adj))
        self.adj_3.clicked.connect(lambda: toNext(levels.level1_adj))
        self.adj_4.clicked.connect(lambda: toNext(levels.level1_adj))
        self.adj_5.clicked.connect(lambda: toNext(levels.level1_adj))

        self.verb_1.clicked.connect(lambda: toNext(levels.level1_verb))
        self.verb_2.clicked.connect(lambda: toNext(levels.level1_verb))
        self.verb_3.clicked.connect(lambda: toNext(levels.level1_verb))
        self.verb_4.clicked.connect(lambda: toNext(levels.level1_verb))
        self.verb_5.clicked.connect(lambda: toNext(levels.level1_verb))

        self.back.clicked.connect(lambda: toBack())


class Level(QMainWindow):
    def __init__(self):
        super(Level, self).__init__()
        loadUi("level_1_1.ui", self)

        cur.execute("SELECT * FROM Words WHERE categoryID = 1")
        rows = cur.fetchall()
        self.back.clicked.connect(lambda: toBack())

        self.dictOFWords1 = dict()
        for row in rows:
            key = row[0]
            values = (row[1], row[2])
            self.dictOFWords1[key] = values
        # self.set_text(self.dictOFWords)
        self.buttonGroup.buttonClicked.connect(lambda btn: self.checking_truth(btn))

    def checking_truth(self, rb):
        selected_answer = rb.text()

        for key, val in self.dictOFWords1.items():
            if val[1] == selected_answer:
                question = val[0]

                if question == self.word.text():
                    self.buttonGroup.setExclusive(False)
                    rb.setChecked(False)
                    self.buttonGroup.setExclusive(True)
                    # selected_answer = ''
                    self.set_text(self.dictOFWords)
                    print('Correct')
                    return

        QMessageBox.about(self, "* * * * * * * * *", "Неверно")
        print('Incorrect')

    def set_text(self, dictWithWord):
        keys = list(dictWithWord.keys())
        random_key = random.choice(keys)
        question = dictWithWord[random_key][0]
        answer = dictWithWord[random_key][1]
        rand = random.randint(0, 3)

        item = self.layoutWithAnswer.itemAtPosition(rand, 0)
        if item:
            label_answ = item.widget()
            label_answ.setText(answer)
        self.word.setText(question)

        answers = []
        for i in range(0, 4):
            if i == rand:
                answers.append(answer)
            else:
                label_answ_text = label_answ.text() if 'label_answ' in locals() else ''
                other_answer = dictWithWord[random.choice(keys)][1]
                while other_answer == answer or other_answer in answers or other_answer == label_answ_text:
                    other_answer = dictWithWord[random.choice(keys)][1]
                answers.append(other_answer)

        for i in range(4):
            item = self.layoutWithAnswer.itemAt(i)
            if item and item.widget():
                item.widget().setText(answers[i])


class CardsWindow(QMainWindow):
    def __init__(self):
        super(CardsWindow, self).__init__()
        loadUi("flashcards.ui", self)

        cur.execute("SELECT * FROM Words WHERE categoryID = 1")
        rows = cur.fetchall()
        self.dictOFWords = dict()

        for row in rows:
            key = row[0]
            values = (row[1], row[2])
            self.dictOFWords[key] = values
        self.set_text(self.dictOFWords)

        self.labshowbtn.hide()
        self.star_1.hide()
        self.star_0.clicked.connect(self.showStarChecked)
        self.star_1.clicked.connect(self.showStarNull)
        self.back.clicked.connect(lambda: toBack())

        self.btn_prev.setEnabled(False)
        self.btn_next.setEnabled(False)
        # if self.rb_know.isChecked() or self.rb_notknow.isChecked():
        #     self.btn_prev.setEnabled(True)
        #     self.btn_next.setEnabled(True)

        self.btn_show.clicked.connect(self.showMeaning)
        self.btn_prev.clicked.connect(lambda: self.set_text(self.dictOFWords))
        self.btn_next.clicked.connect(lambda: self.set_text(self.dictOFWords))

    def set_text(self, dictWithWord):
        keys = list(dictWithWord.keys())
        random_key = random.choice(keys)
        question = dictWithWord[random_key][0]
        answer = dictWithWord[random_key][1]
        self.labword.setText(question)
        self.labshowbtn.setText(answer)
        self.btn_show.show()

        if not self.rb_notknow.isChecked():
            self.showStarChecked()

        self.btn_prev.setEnabled(False)
        self.btn_next.setEnabled(False)

        self.showStarNull()

        # не срабатывает обнуление, печаль
        self.rb_know.setChecked(False)
        self.rb_notknow.setChecked(False)

    def showStarNull(self):
        self.star_1.hide()
        self.star_0.show()

    def showStarChecked(self):
        word_to_insert = self.labword.text()
        f = open('text.txt', 'r')
        name = f.read()
        f.close()
        value = cur.execute(f"SELECT * FROM UserStars WHERE word = '{word_to_insert}'").fetchall()
        if len(value) == 0:
            cur.execute(f"INSERT INTO UserStars(word, userName) VALUES('{word_to_insert}', '{name}')")
            db.commit()
        else:
            pass
        self.star_0.hide()
        self.star_1.show()

    def showMeaning(self):
        self.labshowbtn.show()
        self.btn_show.hide()
        self.btn_prev.setEnabled(True)
        self.btn_next.setEnabled(True)


class SetWindow(QMainWindow):
    def __init__(self):
        super(SetWindow, self).__init__()
        loadUi("settings.ui", self)
        self.dark_mode.clicked.connect(lambda: apply_stylesheet(app, theme='dark_blue.xml'))
        self.light_mode.clicked.connect(lambda: apply_stylesheet(app, theme='light_blue.xml'))
        self.default_2.clicked.connect(lambda: apply_stylesheet(app, theme='default'))

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
            toNext(MainLogged)
        else:
            toNext(RegisterWindow)

    @check_input
    def auth(self):
        name = self.email_login.text()
        passw = self.password_login.text()
        self.check_db.thr_login(name, passw)
        f = open('text.txt', 'w')
        f.write(name)
        f.close()


def boolean_signal(value):
    if value:
        toBack()
    else:
        toNext(MainLogged)


class RegisterWindow(QMainWindow):
    def __init__(self):
        super(RegisterWindow, self).__init__()
        loadUi("register_window.ui", self)
        # self.back.clicked.connect(lambda: toBack())
        self.register_new.clicked.connect(self.reg)
        self.base_line_edit = [self.username_new, self.email_new, self.password_new]
        self.check_db = CheckThread()
        self.check_db.Boolean_signal.connect(boolean_signal)
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

    @check_input
    def reg(self):
        name = self.username_new.text()
        mail = self.email_new.text()
        passw = self.password_new.text()
        self.check_db.thr_register(name, mail, passw)
        f = open('text.txt', 'w')
        f.write(name)
        f.close()


class BaseDictionary(QMainWindow):
    def __init__(self):
        super(BaseDictionary, self).__init__()
        loadUi("dictionary_noneuser.ui", self)
        self.params = {}
        self.con = sqlite3.connect('project2024.db')
        self.back.clicked.connect(lambda: toBack())

        self.selectGenres()
        self.search_2.clicked.connect(self.select)

        self.search.clicked.connect(self.searchWord)

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["* * *"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setStyleSheet("font-size: 12pt;")

    def selectGenres(self):
        req = "SELECT * FROM Categories"
        curs = self.con.cursor()
        for value, key in curs.execute(req).fetchall():
            self.params[key] = value
        self.comboBox.addItems(list(self.params.keys()))

    def select(self):
        req = "SELECT * FROM Words WHERE categoryID = ?"

        category = self.params.get(self.comboBox.currentText())
        cat_1 = int(category)
        curs = self.con.cursor()
        result = curs.execute(req, (cat_1,)).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(7)
        for i, row in enumerate(result):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)

    def searchWord(self):
        curs = self.con.cursor()
        word_entered = self.enter_a_word.text()
        result = curs.execute("SELECT word, translation1, translation2 FROM Words WHERE word = ?", (word_entered,)).fetchall()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(result))

        for i, row in enumerate(result):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)


class AdvDictionary(QMainWindow):
    def __init__(self):
        super(AdvDictionary, self).__init__()
        loadUi("dictionary_advanced.ui", self)
        self.to_add_word.clicked.connect(lambda: toNext(AddingWords))
        self.to_change_word.clicked.connect(lambda: toNext(ChangingWords))
        self.back.clicked.connect(lambda: toBack())

        self.params = {}
        self.con = sqlite3.connect('project2024.db')

        self.selectGenres()
        self.search_2.clicked.connect(self.select)
        self.search.clicked.connect(self.searchWord)

        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["* * *"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setStyleSheet("font-size: 12pt;")

    def selectGenres(self):
        req = "SELECT * FROM Categories"
        curs = self.con.cursor()
        for value, key in curs.execute(req).fetchall():
            self.params[key] = value
        self.comboBox.addItems(list(self.params.keys()))

    def select(self):
        req = "SELECT word, translation1, translation2, imageLink, sentence FROM Words WHERE categoryID = ?"

        genre = self.params.get(self.comboBox.currentText())
        genre_1 = int(genre)
        curs = self.con.cursor()
        result = curs.execute(req, (genre_1,)).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(5)
        for i, row in enumerate(result):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)

    def searchWord(self):
        res = "SELECT word, translation1, translation2, imageLink, sentence FROM Words WHERE word = ?"
        word_entered = self.enter_a_word.text()
        curs = self.con.cursor()
        result = curs.execute(res, (word_entered,)).fetchall()

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)

        for i, row in enumerate(result):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i, j, item)


class AddingWords(QMainWindow):
    def __init__(self):
        super(AddingWords, self).__init__()
        loadUi("adding_new_word.ui", self)

        self.check_db = CheckThread()
        self.check_db.Boolean_signal.connect(boolean_signal)
        self.check_db.my_signal.connect(self.signal_handler)
        self.add_word.clicked.connect(self.auth)
        self.back.clicked.connect(lambda: toBack())

    def signal_handler(self, value):
        QMessageBox.about(self, "* * * * * * * * *", value)

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

        sav = 0
        if s:
            sav = 1
        elif a:
            sav = 2
        elif v:
            sav = 3
        elif abbr:
            sav = 4

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

    @staticmethod
    def boolean_signal(value):
        if value:
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

        sav = 0
        if s:
            sav = 1
        elif a:
            sav = 2
        elif v:
            sav = 3
        elif abbr:
            sav = 4

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

# if dark_theme:
#     apply_stylesheet(app, theme='dark_blue.xml')
# if not dark_theme:
#     apply_stylesheet(app, theme='light_blue.xml')

widget.addWidget(main_window)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

sys.exit(app.exec_())
