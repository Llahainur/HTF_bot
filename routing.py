from classes import Person
from bd_class import readdata

recs = readdata()


def recs_to_arr(recs):
    P_arr=[]
    for row in recs:
        arr = (row[0], [row[2], row[3]], [row[5], row[6]], row[8])
        P_arr.append(arr)
        n = '''print("Имя:", row[0])
        print("Тел:", row[1])
        print("ar_lat:", row[2])
        print("ar_lon:", row[3])
        print("ar_addr:", row[4])
        print("des_lat:", row[5])
        print("des_lon:", row[6])
        print("des_addr:", row[7])
        print("is_driver:", row[8], end="\n\n")'''
    return P_arr

if __name__ == "__main__":
    print(recs_to_arr(recs))
