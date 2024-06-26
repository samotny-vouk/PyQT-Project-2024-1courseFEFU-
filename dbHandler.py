import hashlib
import sqlite3
import re
db = sqlite3.connect('project2024.db')
cur = db.cursor()


def user_hash(my_hash):
    hash_object = hashlib.sha256(my_hash.encode()).hexdigest()
    return hash_object


def login(name_or_mail, passw, signal, bool_signal):
    cur.execute(f'SELECT * FROM Users WHERE userName == "{name_or_mail}" OR userMail == "{name_or_mail}"')
    value = cur.fetchall()
    value1 = user_hash(passw + "256")
    if value and value[0][3] == value1:
        # print(is_logged)
        bool_signal.emit(True)
        # signal.emit('Вход выполнен')
    else:
        bool_signal.emit(False)
        signal.emit('Такой учётной записи нет. Предлагаем зарегистрироваться')


def register(login, mail, passw, signal, bool_signal):
    # email_valid = True
    pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
    if re.match(pattern, mail) is not None:
        global email_valid
        email_valid = True
    else:
        email_valid = False
    cur.execute(f'SELECT * FROM Users WHERE userName="{login}" OR userMail="{mail}"')
    value = cur.fetchone()

    value1 = user_hash(passw + "256")
    if value:
        bool_signal.emit(True)
        signal.emit("Учётная запись '{mail}' уже существует. Предлагаем войти")
    elif not value and not email_valid:
        signal.emit('Введите валидную почту')
    else:
        cur.execute(f"INSERT INTO Users(userName, userMail, userHash) VALUES('{login}', '{mail}', '{value1}')")
        bool_signal.emit(False)
        signal.emit('Приятного приключения')
        db.commit()


def new_word(word, translate1, translate2, sav, sentence, imgLink, signal, bool_signal):
    cur.execute(f'SELECT * FROM Words WHERE word="{word}"')
    value = cur.fetchall()

    if value:
        bool_signal.emit(False)
        signal.emit("The word is already in dictionary")
    else:
        bool_signal.emit(True)
        signal.emit("The insertion completed")
        cur.execute(f"INSERT INTO Words(word, translation1, translation2, categoryID, sentence, imageLink) VALUES('{word}', '{translate1}', '{translate2}', '{sav}', '{sentence}', '{imgLink}')")
        db.commit()


def change_word(word, translate1, translate2, sav, sentence, imgLink, signal, bool_signal):
    cur.execute(f'SELECT * FROM Words WHERE word="{word}"')
    value = cur.fetchall()

    if value:
        cur.execute(f"UPDATE Words SET translation1 = '{translate1}', translation2 = '{translate2}', categoryID = '{sav}', sentence = '{sentence}', imageLink = '{imgLink}' WHERE word = '{word}'")
        db.commit()
        bool_signal.emit(True)
        signal.emit("The update completed")
    else:
        bool_signal.emit(False)
        signal.emit("The word is not in this dictionary")

