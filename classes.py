from geocode import request


def dist(geocode_1, geocode_2):
    dX = float(geocode_1['lat']) - float(geocode_2['lat'])  # широта
    dY = float(geocode_1['lon']) - float(geocode_2['lon'])  # долгота
    return ((dX * 111.111) ** 2 + (dY * 61.8) ** 2) ** 0.5


class Person(object):
    def __init__(self, addr_arr, addr_dest, name, phone, is_driver):
        self.addr_arr = addr_arr
        self.addr_dest = addr_dest
        self.name = name
        self.phone = phone
        self.geocode_arr = request(addr_arr)
        self.geocode_dest = request(addr_dest)
        self.is_driver = is_driver



if __name__ == "__main__":
    P = Person("Москва", "Казань", "Вася", "89898989898", True)
    print(P.geocode_arr)
    print(P.name, dist(P.geocode_arr, P.geocode_dest))
    print(P.geocode_arr["addr"])
