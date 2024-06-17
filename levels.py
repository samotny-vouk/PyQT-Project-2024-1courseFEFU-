import random
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QButtonGroup
import sqlite3

# from PIL import Image
# from urllib.request import urlopen
# url = "https://i.pinimg.com/236x/24/15/21/24152197af38deb718eb730992d441d0.jpg"
# try:
#     image = Image.open(urlopen(url))
#     image.show()
# except: pass

db = sqlite3.connect('project2024.db')
cur = db.cursor()


class level1_sub(QMainWindow):
    def __init__(self):
        super(level1_sub, self).__init__()
        loadUi("quiz.ui", self)

        self.next.clicked.connect(lambda: self.set_text(self.dictOFWords))
        self.prev.clicked.connect(lambda: self.set_text(self.dictOFWords))
        cur.execute("SELECT * FROM Words WHERE categoryID = 1")
        rows = cur.fetchall()

        self.dictOFWords = dict()
        for row in rows:
            key = row[0]
            values = (row[1], row[2])
            self.dictOFWords[key] = values
        self.set_text(self.dictOFWords)
        self.buttonGroup.buttonClicked.connect(lambda btn: self.checking_truth(btn))

    def checking_truth(self, rb):
        selected_answer = rb.text()

        for key, val in self.dictOFWords.items():
            if val[1] == selected_answer:
                question = val[0]

                if question == self.word.text():
                    self.buttonGroup.setExclusive(False)
                    rb.setChecked(False)
                    self.buttonGroup.setExclusive(True)
                    # selected_answer = ''
                    # QMessageBox.about(self, "* * * * * * *", "Верно")
                    self.set_text(self.dictOFWords)
                    print('Correct')
                    return

        QMessageBox.about(self, "* * *", "Неверно")
        print('Incorrect')

    def set_text(self, dictWithWord):
        keys = list(dictWithWord.keys())
        random_key = random.choice(keys)
        question = dictWithWord[random_key][0]
        answer = dictWithWord[random_key][1]
        rand = random.randint(0, 3)

        item = self.gridLayout.itemAtPosition(rand, 0)
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
            item = self.gridLayout.itemAt(i)
            if item and item.widget():
                item.widget().setText(answers[i])

# class level2_sub(QMainWindow):
#     def __init__(self):
#         super(level2_sub, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level3_sub(QMainWindow):
#     def __init__(self):
#         super(level3_sub, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level4_sub(QMainWindow):
#     def __init__(self):
#         super(level4_sub, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level5_sub(QMainWindow):
#     def __init__(self):
#         super(level5_sub, self).__init__()
#         loadUi("quiz.ui", self)


class level1_adj(QMainWindow):
    def __init__(self):
        super(level1_adj, self).__init__()
        loadUi("quiz.ui", self)
        self.buttonGroup = QButtonGroup(self.gridLayout)
        self.buttonGroup.addButton(self.opt_1, id=1)
        self.buttonGroup.addButton(self.opt_2, id=2)
        self.buttonGroup.addButton(self.opt_3, id=3)
        self.buttonGroup.addButton(self.opt_4, id=4)
        self.buttonGroup.addButton(self.opt_5, id=5)

        self.next.clicked.connect(lambda: self.set_text(self.dictOFWords))
        self.prev.clicked.connect(lambda: self.set_text(self.dictOFWords))
        cur.execute("SELECT * FROM Words WHERE categoryID = 2")
        rows = cur.fetchall()

        self.dictOFWords = dict()
        for row in rows:
            key = row[0]
            values = (row[1], row[2])
            self.dictOFWords[key] = values
        # self.set_text(self.dictOFWords)
        self.buttonGroup.buttonClicked.connect(lambda btn: self.checking_truth(btn))

    def checking_truth(self, rb):
        selected_answer = rb.text()

        for key, val in self.dictOFWords.items():
            if val[1] == selected_answer:
                question = val[0]

                if question == self.word.text():
                    self.buttonGroup.setExclusive(False)
                    rb.setChecked(False)
                    self.buttonGroup.setExclusive(True)
                    # selected_answer = ''
                    # QMessageBox.about(self, "* * * * * * *", "Верно")
                    self.set_text(self.dictOFWords)
                    print('Correct')
                    return

        QMessageBox.about(self, "* * *", "Неверно")
        print('Incorrect')

    def set_text(self, dictWithWord):
        keys = list(dictWithWord.keys())
        random_key = random.choice(keys)
        question = dictWithWord[random_key][0]
        answer = dictWithWord[random_key][1]
        rand = random.randint(0, 4)

        item = self.gridLayout.itemAtPosition(rand, 0)
        if item:
            label_answ = item.widget()
            label_answ.setText(answer)
        self.word.setText(question)

        answers = []
        for i in range(0, 5):
            if i == rand:
                answers.append(answer)
            else:
                label_answ_text = label_answ.text() if 'label_answ' in locals() else ''
                other_answer = dictWithWord[random.choice(keys)][1]
                while other_answer == answer or other_answer in answers or other_answer == label_answ_text:
                    other_answer = dictWithWord[random.choice(keys)][1]
                answers.append(other_answer)

        for i in range(0, 4):
            item = self.gridLayout.itemAt(i)
            if item and item.widget():
                item.widget().setText(answers[i])


# class level2_adj(QMainWindow):
#     def __init__(self):
#         super(level2_adj, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level3_adj(QMainWindow):
#     def __init__(self):
#         super(level3_adj, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level4_adj(QMainWindow):
#     def __init__(self):
#         super(level4_adj, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level5_adj(QMainWindow):
#     def __init__(self):
#         super(level5_adj, self).__init__()
#         loadUi("quiz.ui", self)
#

class level1_verb(QMainWindow):
    def __init__(self):
        super(level1_verb, self).__init__()
        loadUi("quiz.ui", self)
        self.buttonGroup = QButtonGroup(self.gridLayout)
        self.buttonGroup.addButton(self.opt_1, id=1)
        self.buttonGroup.addButton(self.opt_2, id=2)
        self.buttonGroup.addButton(self.opt_3, id=3)
        self.buttonGroup.addButton(self.opt_4, id=4)
        self.buttonGroup.addButton(self.opt_5, id=5)

        self.next.clicked.connect(lambda: self.set_text(self.dictOFWords))
        self.prev.clicked.connect(lambda: self.set_text(self.dictOFWords))
        cur.execute("SELECT * FROM Words WHERE categoryID = 3")
        rows = cur.fetchall()

        self.dictOFWords = dict()
        for row in rows:
            key = row[0]
            values = (row[1], row[2])
            self.dictOFWords[key] = values
        self.set_text(self.dictOFWords)
        self.buttonGroup.buttonClicked.connect(lambda btn: self.checking_truth(btn))

    def checking_truth(self, rb):
        selected_answer = rb.text()

        for key, val in self.dictOFWords.items():
            if val[1] == selected_answer:
                question = val[0]

                if question == self.word.text():
                    self.buttonGroup.setExclusive(False)
                    rb.setChecked(False)
                    self.buttonGroup.setExclusive(True)
                    # selected_answer = ''
                    # QMessageBox.about(self, "* * * * * * *", "Верно")
                    self.set_text(self.dictOFWords)
                    print('Correct')
                    return

        QMessageBox.about(self, "* * *", "Неверно")
        print('Incorrect')

    def set_text(self, dictWithWord):
        keys = list(dictWithWord.keys())
        random_key = random.choice(keys)
        question = dictWithWord[random_key][0]
        answer = dictWithWord[random_key][1]
        rand = random.randint(0, 4)

        item = self.gridLayout.itemAtPosition(rand, 0)
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

        for i in range(0, 4):
            item = self.gridLayout.itemAt(i)
            if item and item.widget():
                item.widget().setText(answers[i])


# class level2_verb(QMainWindow):
#     def __init__(self):
#         super(level2_verb, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level3_verb(QMainWindow):
#     def __init__(self):
#         super(level3_verb, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level4_verb(QMainWindow):
#     def __init__(self):
#         super(level4_verb, self).__init__()
#         loadUi("quiz.ui", self)
#
#
# class level5_verb(QMainWindow):
#     def __init__(self):
#         super(level5_verb, self).__init__()
#         loadUi("quiz.ui", self)


class level_logic(QMainWindow):
    pass