from classes import Person
from bd_class import readdata
from math import cos


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Path:
    def __init__(self, pointS, pointE):
        self.pointS = pointS
        self.pointE = pointE


def point_diff(point1=Point, point2=Point):
    Klat = 111.12
    Klon = 64  # по Москве
    return round(((abs((point1.x - point2.x) * Klat) ** 2 + abs((point1.y - point2.y) * Klon) ** 2) ** 0.5), 2)


def path_diff(path1=Path, path2=Path):
    startdiff = point_diff(path1.pointS, path2.pointS)
    enddiff = point_diff(path1.pointE, path2.pointE)
    diff = startdiff * enddiff
    return round(diff, 4), startdiff, enddiff


def mass_path_diff(arr_of_Paths=[Path]):
    res=[[]]
    for i in range(len(arr_of_Paths)):
        for j in range(i, len(arr_of_Paths)):
            res[i][j] = path_diff(arr_of_Paths[i], arr_of_Paths[j])
        print(res[i])
    return res


def recs_to_arr(records):
    P_array = []
    for row in records:
        p1 = Point(float(row[2]), float(row[3]))
        p2 = Point(float(row[5]), float(row[6]))
        path = Path(p1, p2)
        # нач, коор конц, водитель?,номер записи
        P_array.append(path)
    return P_array


if __name__ == "__main__":
    recs = readdata()
    P_arr = recs_to_arr(recs)
    print("Записей принято: " + str(len(P_arr)))
    P1 = Path
    P2 = Path
    P1, P2 = P_arr[0], P_arr[1]
    print(mass_path_diff(P_arr))
