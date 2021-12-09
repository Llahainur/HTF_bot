import sqlite3 as sql
from classes import Person


def array_maker(Pers):
    arr = (str(Pers.name), str(Pers.phone), float(Pers.geocode_arr['lat']), float(Pers.geocode_arr['lon']),
           str(Pers.geocode_arr['addr']), float(Pers.geocode_dest['lat']), float(Pers.geocode_dest['lon']),
           str(Pers.geocode_dest['addr']),int(Pers.is_driver))#isdriver
    print(arr)
    return arr


class BD(object):
    def __init__(self):
        self.name = "data.db"

    def adddata(P):
        connect = sql.connect("data.db")
        curs = connect.cursor()
        data = array_maker(P)
        curs.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?);"
                     , data)
        connect.commit()
        print(connect.execute("SELECT * FROM users;"))
        connect.close()



if __name__ == "__main__":
    P = Person("Москва", "Казань", "Вася", "89898989898", True)
    conn = sql.connect('data.db')
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
    BD.adddata(P)

