import sqlite3
import hashlib


def user_hash(my_hash):
    hash_object = hashlib.sha256(my_hash.encode()).hexdigest()
    return hash_object
    # hash_object.hexdigest()


def login(name_or_mail, passw):
    con = sqlite3.connect('films.db')
    cur = con.cursor()
    # username = con.cursor

    cur.execute(f'SELECT * FROM Users WHERE userName == "{name_or_mail}" OR userMail == "{name_or_mail}"')
    value = cur.fetchall()
    # username.execute(f'SELECT userName FROM Users WHERE userName == "{name_or_mail}" OR userMail == "{name_or_mail}"')

    value1 = user_hash(passw + "256")

    if value != [] and value1 == value[0][3]:
        is_logged = True
        # signal.emit(f'Приветствуем, {login}')
    else:
        is_logged = False
        # signal.emit('Проверьте правильность ввода')
    cur.close()
    con.close()

    return is_logged


def register(login, mail, passw):
    con = sqlite3.connect('films.db')
    cur = con.cursor()

    value = cur.execute(f'SELECT * FROM Users WHERE userName = "{mail}";').fetchall()

    value1 = user_hash(passw + "256")

    if value != []:
        pass
        # signal.emit('vfgcbgfdcfsd')
    elif value == []:
        cur.execute(f'INSERT INTO Users (userName, userMail, userHash) VALUES ("{login}", "{mail}", "{value1}")')
        # signal.emit('fdgbgtfbgfd')
    cur.close()
    con.close()
    return value1


username = "name"
email = "mail"
password = "srgbherwsdfdewas"
hashed1 = register(username, email, password)
print(hashed1)


def wording():
    pass

def take_user_name():
    pass