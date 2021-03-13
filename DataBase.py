# import sqlite3
#
#
#
# def add_to_database_customers(name, chat_id, subject, data_time, order_text):
#     db = sqlite3.connect(r'C:\Users\dimak\Downloads\SQLiteStudio-3.2.1\SQLiteStudio\db_Bot_customer')
#     cursor = db.cursor()
#     print(cursor.execute('select * from Customers').fetchall())
#     cursor.execute('insert into Customers ("name", "chat_id", "subject", "order_text") values (?,?,?,?)',(name, chat_id, subject, order_text) )
#     db.commit()
# add_to_database('n','2','f','g')
