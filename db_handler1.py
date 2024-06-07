import hashlib
import sqlite3
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
        signal.emit('Вход выполнен')
    else:
        bool_signal.emit(False)
        signal.emit('Введён неправильный логин или пaроль')

        # print(is_logged)


def register(login, mail, passw, signal, bool_signal):
    cur.execute(f'SELECT * FROM Users WHERE userName="{login}" OR userMail="{mail}"')
    value = cur.fetchone()

    value1 = user_hash(passw + "256")
    if value:
        bool_signal.emit(True)
        signal.emit('Такой ник есть')
    else:
        cur.execute(f"INSERT INTO Users(userName, userMail, userHash) VALUES('{login}', '{mail}', '{value1}')")
        bool_signal.emit(False)
        signal.emit('Новый пользователь!!!')
        db.commit()


def new_word(word, translate1, translate2, sav, sentence, imgLink):
    cur.execute(f'SELECT * FROM Words WHERE word="{word}"')
    value = cur.fetchone()

    if value:
        print("The word is already in dictionary")
    else:
        cur.execute(f"INSERT INTO Words(word, translation1, translation2, category, sentence, imageLink) VALUES('{word}', '{translate1}', '{translate2}, {sav}, {sentence}, {imgLink}')")
        db.commit()
        print("The insertion completed")
