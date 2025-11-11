import json
import os

def get_file_path(filename):
   
    base_path = os.path.dirname(os.path.abspath(__file__))   
    file_path = os.path.join(base_path, "..", "..", "files", filename) 
    return os.path.normpath(file_path)  

def define_id(filename):
    path = get_file_path(filename)

    with open(path, "r", encoding="utf-8") as file:
        data = file.read().split("\n")

    ide = 1
    dictionary = []

    for key in range(len(data) - 1):
        if data[key].strip() != "":
            dictionary.append(json.loads(data[key]))

    ids = [item["id"] for item in dictionary if "id" in item]

    if ids:  
        while True:
            if ide in ids:
                ide += 1
            else:
                break
    else:
        ide = 1

    return ide

def return_exist(filename):
    path = get_file_path(filename)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def validate_exist(filename, name):
    container = return_exist(filename)
    result = [False, None]

    for item in container:
        if name.lower() == item["name"].lower():
            result[0] = True
            result[1] = item["id"]
            return result
    return result

def valid_lot(product, lot):
    container = return_exist("stocktaking.json")

    for item in container:
        if item["name"].lower() == product.lower() and item["lot"] < lot:
            return False
    return True

def valid_date(date):
    if date == '' or len(date) != 10:
        print("Invalid date")
        return False

    list_date = date.split('-')
    try:
        year = int(list_date[0])
        month = int(list_date[1])
        day = int(list_date[2])
    except:
        print("Invalid format (YYYY-MM-DD expected)")
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

