import json
from child_classes.path_manager import get_file_path # funcion para la ruta dinamica

def define_id(path):
    file = open(f"{path}", "r")
    data = file.read()
    data = data.split("\n")
    ide = 1
    dictionary = []
    for key in range(len(data) - 1):
        dictionary.append(json.loads(data[key]))

    ids = []
    for i in range(len(dictionary)):
        ids.append(dictionary[i]["id"])

    if ids is not None or ids != "null" or ids == []:
        while True:
            if ide in ids: ide += 1
            else: break
    else: ide = 1
    return ide

def return_exist(path):
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def validate_exist(path, name):
    container = return_exist(path)
    x = [False, None]

    for i in range(len(container)):
        if name in container[i]["name"] or name.lower() == container[i]["name"].lower():
            x[0] = True
            x[1] = container[i]["id"]
            return x
    return x


def valid_lot(product, lot):
<<<<<<< HEAD
    container = return_exist("C:/Users/ESTUDIANTE/Documents/music/music-store-console/files/stocktaking.json")
=======
    container = return_exist(get_file_path("stocktaking.json")) # Dinamico
>>>>>>> joss

    for i in range(len(container)):
        if container[i]["name"].lower() == product.lower() and container[i]["lot"] < lot:
            return False
    return True


def valid_date(date):
    if date == '' or len(date) != 10:
        print("Invalid date")
        return False

    list_date = date.split(sep='-')
    try:
        day = int(list_date[2])
        year = int(list_date[0])
        month = int(list_date[1])
    except:
        return False

    if not (1 <= day <= 31):
        print("Invalid day")
        return False
    elif not (1 <= month <= 12):
        print("Invalid month")
        return False
    elif year > 2025:
        print("Invalid year")
        return False
    return True

#primer cambio
#segundo cambio