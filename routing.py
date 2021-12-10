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
    return (abs(point1.x - point2.x) ** 2 + abs(point1.y - point2.y) ** 2) ** 0.5


def path_diff(path1=Path, path2=Path):
    startdiff = point_diff(path1.pointS, path2.pointS)
    enddiff = point_diff(path1.pointE, path2.pointE)
    diff = startdiff * enddiff
    return diff, startdiff, enddiff


def recs_to_arr(records):
    P_array = []
    i = 0
    for row in records:
        p1 = Point(float(row[2]), float(row[3]))
        p2 = Point(float(row[5]), float(row[6]))
        path = Path(p1, p2)
        # нач, коор конц, водитель?,номер записи
        P_array.append(path)
        i = i + 1
    return P_array


if __name__ == "__main__":
    recs = readdata()
    P_arr = recs_to_arr(recs)
    print("Записей принято: " + str(len(P_arr)))

    P1=Path
    P2=Path
    P1,P2=P_arr[0],P_arr[1]
    print(path_diff(P1,P2))

