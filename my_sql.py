import sqlite3


def add_to_database(chat_id,first_name, order_text = 'Тестовый текст'):
    db = sqlite3.connect("Test.db")
    cursor = db.cursor()
    cursor.execute("insert into customers_table values(:chat_id,:nickname,:order_text)",
                   {"chat_id": 8943212, "nickname": 'test', "order_text": 'Hello'})
    db.commit()