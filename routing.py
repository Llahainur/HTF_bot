from classes import Person
from bd_class import readdata
from math import cos

recs = readdata()


def dist(arriv, destin):  # расстояние по формуле пифагора с поправкой
    Rlat = 111.32
    Rlon = 40075.696 * cos(arriv[0]) / 360
    return (((arriv[0] - destin[0]) * Rlat) ** 2 + (
                (arriv[1] - destin[1]) * Rlon) ** 2) ** 0.5  # lat широтв, lon долгота


def differ(route1, route2):  # расстояние между началами и концами маршрутов
    distantion = dist(route1[1], route2[1]), dist(route1[2], route2[2])
    return distantion


def recs_to_arr(recs):
    P_arr = []
    i=0
    for row in recs:
        arr = (row[0], [float(row[2]), float(row[3])], [float(row[5]), float(row[6])], bool(row[8]))# имя, коор
        # нач, коор конц, водитель?,номер записи
        P_arr.append(arr)
        i=i+1
    return P_arr

if __name__ == "__main__":
    P_arr = recs_to_arr(recs)
    print(P_arr)  # первый индекс-номер записи, второй - начало (1) или конец (2) маршрута
    print(differ(P_arr[0], P_arr[1]))
