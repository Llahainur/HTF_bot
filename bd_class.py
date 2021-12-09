import sqlite3 as sql
from classes import *


def array_maker(Pers):
    arr = (str(Pers.name), str(Pers.phone), float(Pers.geocode_arr['lat']), float(Pers.geocode_arr['lon']),
           str(Pers.geocode_arr['addr']), float(Pers.geocode_dest['lat']), float(Pers.geocode_dest['lon']),
           str(Pers.geocode_dest['addr']), int(Pers.is_driver))
    return arr


class BD(object):
    def __init__(self):
        self.name = "data.db"

    def adddata(P):
        connect = sql.connect("data.db")
        curs = conn.cursor()
        id = float(P.geocode_arr["lat"]) * float(P.geocode_arr["lon"]) + float(P.geocode_dest["lat"]) + float(
            P.geocode_dest["lat"])  # достаточно уникальный набор данных

        data = array_maker(P)
        cur.execute("INSERT INTO users VALUES(?,?,?,?,?,?,?,?,?);", array_maker(P))
        connect.commit()


if __name__ == "__main__":
    P = Person("Москва", "Казань", "Вася", "89898989898", True)
    conn = sql.connect('data.db')
    cur = conn.cursor()
    print(array_maker(P))
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY,
       name TEXT,
       phone TEXT,
       ar_lat REAL,
       ar_lon REAL,
       ar_addr TEXT,
       dest_lat REAL,
       dest_lon REAL
       dest_addr TEXT
       isdriver INT
       );
    """)
    BD.adddata(P)

