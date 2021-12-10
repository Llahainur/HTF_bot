from classes import Person
from bd_class import readdata
from math import cos


def distantion(ar1, ar2):
    x1 = ar1[0]
    y1 = ar1[1]
    x2 = ar2[0]
    y2 = ar2[1]
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5



def recs_to_arr(records):
    P_array = []
    geo_arr = []
    i = 0
    for row in records:
        num = (row[2] * row[3]) % (row[5] * row[6])
        num = i
        arr = ([float(row[2]), float(row[3])], [float(row[5]), float(row[6])], bool(row[8]))  # имя, коор
        # нач, коор конц, водитель?,номер записи
        P_array.append(arr)
        i = i + 1
    return P_array


if __name__ == "__main__":
    recs = readdata()
    P_arr = recs_to_arr(recs)
    print("Записей принято: " + str(len(P_arr)))
    print(P_arr)  # первый индекс-номер записи, второй - начало (1) или конец (2) маршрута
