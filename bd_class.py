import sqlite3 as sql
from classes import *


def array_maker(Pers):
    arr = []
    arr.append(str(Pers.name))
    arr.append(str(Pers.phone))
    arr.append(float(Pers.geocode_arr['lat']))
    arr.append(float(Pers.geocode_arr['lon']))
    arr.append(str(Pers.geocode_arr['addr']))
    arr.append(float(Pers.geocode_dest['lat']))
    arr.append(float(Pers.geocode_dest['lon']))
    arr.append(str(Pers.geocode_dest['addr']))
    arr.append(int(Pers.is_driver))
    return arr

class BD(object):
    def __init__(self):
        self.name = "data.db"

    def adddata(P):
        conn = sql.connect("data.db")
        cur = conn.cursor()
        id = float(P.geocode_arr["lat"]) * float(P.geocode_arr["lon"]) + float(P.geocode_dest["lat"]) + float(
            P.geocode_dest["lat"])  # достаточно
        # уникальный набор данных
        print(array_maker(P))
        #cur.executemany("")
        #conn.commit()


if __name__ == "__main__":
    P = Person("Москва", "Казань", "Вася", "89898989898", True)
    conn = sql.connect('data.db')
    cur = conn.cursor()

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
    conn.commit()
    BD.adddata(P)
