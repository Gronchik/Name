# Всё про работу с SQLite

import sqlite3

dbName = 'Arkadia.db'


def bdCheckId(userid) -> bool:
    connection = sqlite3.connect(dbName)
    cur = connection.cursor()
    if cur.execute('''SELECT username FROM users where userid = ?''', (userid,)).fetchone() is not None:
        return True
    else:
        return False


def bdStatistic(userid):
    connection = sqlite3.connect(dbName)
    cur = connection.cursor()
    data = cur.execute('''SELECT hitpoints, stamina, money, reputation, speed, experience '''
                       '''FROM stats where userid =?''', (userid,)).fetchall()
    connection.close()
    return data[0]


def bdPasteUser(userid, game_name='Gamer'):
    connection = sqlite3.connect(dbName)
    cur = connection.cursor()
    cur.execute('''INSERT INTO users (userid, username)
                VALUES (?,?)''', (userid, game_name))
    cur.execute('''INSERT INTO inventory (userid, inventory) VALUES (?,?)''', (userid, '0;0;0;0;0;0;0;0;0'))
    cur.execute('''INSERT INTO stats (userid, hitpoints, speed, money, stamina, reputation, experience)'''
                ''' VALUES (?,?,?,?,?,?,?)''', (userid, 90, 1, 0, 100, 0, 0))
    connection.commit()
    connection.close()


def bdChangeStats(userid, hitpoints=0, speed=0, money=0, stamina=0, reputation=0, experience=0):
    connection = sqlite3.connect(dbName)
    cur = connection.cursor()
    cur.execute('''UPDATE stats SET hitpoints = hitpoints + ?, speed = speed + ?, money = money + ?, stamina = 
                stamina + ?, reputation = reputation + ?, experience = experience + ?'''
                ''' WHERE userid =?''', (hitpoints, speed, money, stamina, reputation, experience, userid))
    connection.commit()
    connection.close()


def bdDeleteId(userid):
    pass


def create_db():
    connection = sqlite3.connect(dbName)
    cur = connection.cursor()
    cur.execute('''CREATE TABLE users (
                userid INTEGER,
                username TEXT
                )''')
    connection.commit()

    cur.execute('''CREATE TABLE inventory (
                userid INTEGER,
                inventory TEXT
                )''')
    connection.commit()

    cur.execute('''CREATE TABLE stats (
                userid INTEGER,
                hitpoints INTEGER,
                speed INTEGER,
                money INTEGER,
                stamina INTEGER,
                reputation INTEGER,
                experience INTEGER
                )''')
    connection.close()
