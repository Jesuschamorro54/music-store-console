import json
import os
<<<<<<< HEAD
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
=======

# ---------------------------
# Función para obtener rutas dinámicas
# ---------------------------
def get_file_path(filename):
    """
    Retorna la ruta absoluta del archivo dentro de la carpeta 'files'
    sin importar desde qué computador se ejecute el proyecto.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))   # ruta actual (este archivo)
    file_path = os.path.join(base_path, "..", "..", "files", filename)  # sube dos niveles y entra en 'files'
    return os.path.normpath(file_path)  # normaliza la ruta (funciona igual en Windows y Linux)


# ---------------------------
# Define el siguiente ID disponible
# ---------------------------
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

    if ids:  # si hay ids existentes
        while True:
            if ide in ids:
                ide += 1
            else:
                break
    else:
        ide = 1

    return ide


# ---------------------------
# Retorna el contenido de un archivo JSON
# ---------------------------
def return_exist(filename):
    path = get_file_path(filename)
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

>>>>>>> 6d1c864ee5396e555d1adaaa4cbc922bcb051c07

# ---------------------------
# Verifica si un elemento ya existe por nombre
# ---------------------------
def validate_exist(filename, name):
    container = return_exist(filename)
    result = [False, None]

    for item in container:
        if name.lower() == item["name"].lower():
            result[0] = True
            result[1] = item["id"]
            return result
    return result

<<<<<<< HEAD
def valid_lot(product, lot):
    file_path = get_file_path("stocktaking.json")
    container = return_exist(file_path)
=======

# ---------------------------
# Valida que el lote sea correcto
# ---------------------------
def valid_lot(product, lot):
    container = return_exist("stocktaking.json")
>>>>>>> 6d1c864ee5396e555d1adaaa4cbc922bcb051c07

    for item in container:
        if item["name"].lower() == product.lower() and item["lot"] < lot:
            return False
    return True

<<<<<<< HEAD
=======

# ---------------------------
# Valida el formato y rango de una fecha
# ---------------------------
>>>>>>> 6d1c864ee5396e555d1adaaa4cbc922bcb051c07
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
<<<<<<< HEAD
    return True
=======
    return True

>>>>>>> 6d1c864ee5396e555d1adaaa4cbc922bcb051c07
