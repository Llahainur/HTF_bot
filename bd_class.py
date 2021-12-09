import sqlite3 as sql
from classes import Person

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


class BD(object):
    def __init__(self):
        self.name = bd_name

    def adddata(self, Pers):
        connect = sql.connect(bd_name)
        curs = connect.cursor()
        data = array_maker(Pers)

        curs.execute("""INSERT INTO users 
        (name,
          phone,
          ar_lat,
          ar_lon,
          ar_addr,
          dest_lat,
          dest_lon,
          dest_addr,
          is_driver) 
          VALUES(?,?,?,?,?,?,?,?,?);"""
                     , data)
        connect.commit()
        print(Pers.name + " addeed to db")
        curs.close()
        # connect.close()

    def readata(self):
        connect = sql.connect(bd_name)
        cursor = connect.cursor()
        connect.execute("SELECT * FROM users")
        records = cursor.fetchall()
        cursor.close()
        connect.close()
        return records


if __name__ == "__main__":
    init_db()
    database = BD
    P1 = Person("Москва, ленинградское ш 11", "Москва ленинградское ш 12", "Додик", "89898933398", True)
    P2 = Person("Москва, парк горького", "Москва, речной вокзал", "Вася", "11111111", False)
    BD.adddata(database, P1)
    BD.adddata(database, P2)
    print(BD.readata(database))
