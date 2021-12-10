from classes import Person
from bd_class import readdata
from math import cos
import time


class Point:  # класс точки. Содержит 2 координаты - широту и долготу (x,y)
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Path:  # класс пути. Содержит две точки - начала и конца пути.
    def __init__(self, pointS, pointE):
        self.pointS = pointS
        self.pointE = pointE


def recs_to_arr(records):
    P_array = []
    for row in records:
        p1 = Point(float(row[2]), float(row[3]))
        p2 = Point(float(row[5]), float(row[6]))
        path = Path(p1, p2)
        P_array.append(path)
    return P_array


def point_diff(point1=Point, point2=Point):  # ищет расстояние между двумя точками, переводя в километры. Точность 5%
    Klat = 111.12
    Klon = 64  # коэфф град->километр, по Москве
    return round(((abs((point1.x - point2.x) * Klat) ** 2 + abs((point1.y - point2.y) * Klon) ** 2) ** 0.5), 2)


def path_diff(path1=Path, path2=Path):
    startdiff = point_diff(path1.pointS, path2.pointS)  # разность по начальным координатам
    enddiff = point_diff(path1.pointE, path2.pointE)  # разность по конечным координатам
    diff = startdiff * enddiff  # разность для обоих коорд. Определяющий критерий
    return round(diff, 4), startdiff, enddiff


def mass_path_diff(arr_of_Paths, search_id):
    l = len(arr_of_Paths)
    res = [0] * l
    for i in range(l):
        res[i] = [0] * l
    found_id = 0

    for i in range(len(arr_of_Paths)):
        for j in range(i + 1, len(arr_of_Paths)):
            res[i][j] = path_diff(arr_of_Paths[i], arr_of_Paths[j])
            found_diff = res[i][j][0]

            if i == search_id and res[i][j][0] < found_diff:
                found_id = [i, j]
                found_diff = res[i][j][0]
            elif j == search_id and res[i][j][0] < found_diff:
                found_id = [i, j]
                found_diff = res[i][j][0]

            print(path_diff(arr_of_Paths[i], arr_of_Paths[j]), i, j)
    return res, found_id, found_diff


if __name__ == "__main__":
    recs = readdata()
    P_arr = recs_to_arr(recs)
    print("Записей принято: " + str(len(P_arr)))
    P1 = Path
    P2 = Path
    P1, P2 = P_arr[0], P_arr[1]
    diff, id, found_d = mass_path_diff(P_arr, 2)
    print(id, found_d)
