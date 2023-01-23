import sqlite3
import random
from config import bot


def create_db():
    global db, cursor
    db = sqlite3.connect('painbot.sqlite3')
    cursor = db.cursor()

    if db:
        print('База данных подключена')

    db.execute("""CREATE TABLE IF NOT EXISTS mentors(
                  id INTEGER PRIMARY KEY,
                  name VARCHAR(50),
                  direction VARCHAR(50),
                  age INTEGER,
                  groupp VARCHAR(50))""")

    db.commit()


async def sql_insert(state):
    async with state.proxy() as data:
        cursor.execute("""INSERT INTO mentors(id, name, direction, age, groupp)
                          VALUES (?, ?, ?, ?, ?)""", tuple(data.values()))

        db.commit()


async def sql_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_mentor = random.choice(result)

    await bot.send_message(
        message.from_user.id,
        f'ID: {random_mentor[0]}\nName: {random_mentor[1]}\nDirection: {random_mentor[2]}\n'
        f'Age: {random_mentor[3]}\nGroup: {random_mentor[4]}'
    )


async def sql_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()
