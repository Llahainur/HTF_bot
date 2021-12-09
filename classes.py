from geocode import request


def dist(geocode_1, geocode_2):
    dX = float(geocode_1['lat']) - float(geocode_2['lat'])  # широта
    dY = float(geocode_1['lon']) - float(geocode_2['lon'])  # долгота
    return ((dX * 111.111) ** 2 + (dY * 61.8) ** 2) ** 0.5


def get_unique_id(P):
    id = float(P.geocode_arr["lat"]) * float(P.geocode_arr["lon"]) + float(P.geocode_dest["lat"]) + float(
        P.geocode_dest["lat"])  # достаточно уникальный набор данных
    return id


class Person(object):
    def __init__(self, addr_arr, addr_dest, name, phone, is_driver):
        self.addr_arr = addr_arr  # не идет в БД
        self.addr_dest = addr_dest  # не идет в БД
        self.name = name
        self.phone = phone
        self.geocode_arr = request(addr_arr)
        self.geocode_dest = request(addr_dest)
        self.is_driver = is_driver



if __name__ == "__main__":
    P = Person("Москва, Ленинградское Ш", "Казань", "Вася", "89898989898", True)
    print(P.array())
