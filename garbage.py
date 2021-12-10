import sqlite3


def read_sqlite_table():
    try:
        sqlite_connection = sqlite3.connect('data.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from users"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")
        for row in records:
            print("Имя:", row[0])
            print("Тел:", row[1])
            print("ar_lat:", row[2])
            print("ar_lon:", row[3])
            print("ar_addr:", row[4])
            print("des_lat:", row[5])
            print("des_lon:", row[6])
            print("des_addr:", row[7])
            print("is_driver:",row[8], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


read_sqlite_table()
