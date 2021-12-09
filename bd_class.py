import sqlite3 as sql
from classes import Person
from geocode import *

bd_name = "data.db"


def init_db():
    conn = sql.connect(bd_name)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
          name,
          phone,
          ar_lat,
          ar_lon,
          ar_addr,
          dest_lat,
          dest_lon,
          dest_addr,
          is_driver)""")
    conn.close()


def array_maker(Pers):
    arr = (str(Pers.name), str(Pers.phone), float(Pers.geocode_arr['lat']), float(Pers.geocode_arr['lon']),
           str(Pers.geocode_arr['addr']), float(Pers.geocode_dest['lat']), float(Pers.geocode_dest['lon']),
           str(Pers.geocode_dest['addr']), int(Pers.is_driver))  # isdriver
    return arr


def adddata(Pers):
    try:
        connect = sql.connect(bd_name)
        curs = connect.cursor()
        data = array_maker(Pers)
        #print("Подключен к SQLite")
        curs.execute("""INSERT INTO users (name, phone,ar_lat,ar_lon,ar_addr,dest_lat,dest_lon,dest_addr,is_driver) 
        VALUES(?,?,?,?,?,?,?,?,?);""", data)
        connect.commit()
        #print(Pers.name, "добавлен в базу")
        curs.close()
        connect.close()
    except sql.Error as error:
        print("Ошибка при чтении SQLite", error)
    finally:
        if connect:
            connect.close()
            #print("Соединение с SQLite закрыто")


def readdata():
    try:
        sqlite_connection = sql.connect('data.db')
        cursor = sqlite_connection.cursor()
        #print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from users"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        #print("Всего строк:  ", len(records))
    except sql.Error as error:
        print("Ошибка при чтении SQLite", error)
    finally:
        if sqlite_connection:
            cursor.close()
            sqlite_connection.close()
            #print("Соединение с SQLite закрыто")
            return records





if __name__ == "__main__":
    init_db()
    P1 = Person("Москва, ленинградское ш 11", "Москва ленинградское ш 12", "Додик", "89898933398", True)
    P2 = Person("Москва, парк горького", "Москва, речной вокзал", "sssssя", "11111111", False)
    #BD.adddata(P1)
    #BD.adddata(P2)
    recs = readdata()
    for row in recs:
        print("Имя:", row[0])
        print("Тел:", row[1])
        print("ar_lat:", row[2])
        print("ar_lon:", row[3])
        print("ar_addr:", row[4])
        print("des_lat:", row[5])
        print("des_lon:", row[6])
        print("des_addr:", row[7])
        print("is_driver:", row[8], end="\n\n")
