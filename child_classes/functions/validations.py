import json
import os
from child_classes.functions.path_utilis import get_file_path
from child_classes.functions.json_utilis import read_json_file

def define_id(path):
    filename = os.path.basename(path)
    dictionary = read_json_file(filename)
    
    ide = 1
    ids = []
    
    for i in range(len(dictionary)):
        ids.append(dictionary[i]["id"])

    if ids:
        while True:
            if ide in ids: 
                ide += 1
            else: 
                break
    
    return ide

def return_exist(path):
    filename = os.path.basename(path)
    return read_json_file(filename)

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
    file_path = get_file_path("stocktaking.json")
    container = return_exist(file_path)

    for i in range(len(container)):
        if container[i]["name"].lower() == product.lower() and container[i]["lot"] < lot:
            return False
    return True

def valid_date(date):
    if date == '' or len(date) != 10:
        print("Invalid date")
        return False

    list_date = date.split('-')
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