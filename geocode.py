# https://nominatim.openstreetmap.org/search.php?q=Казань+магистральная+улица+77&format=jsonv2
import json
import requests


def validate_addr_str(str):
    str.replace(" ", "+")
    return str


def request(addr_in):
    try:
        addr = validate_addr_str(addr_in)

        response = requests.get(
            "https://nominatim.openstreetmap.org/search.php?q=" + addr + "&format=jsonv2")
        j_geo = json.loads(response.text)
        lat = j_geo[0]["lat"]
        lon = j_geo[0]["lon"]
        addr = j_geo[0]["display_name"]
        return {"lat": lat, "lon": lon, "addr": addr}
    except:
        print("http error")


if __name__ == "__main__":
    res = request("Москва Ленинские горы 1")
    print(res)
