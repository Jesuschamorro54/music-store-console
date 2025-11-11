import json
import os


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


# ---------------------------
# Valida que el lote sea correcto
# ---------------------------
def valid_lot(product, lot):
    container = return_exist("stocktaking.json")

    for item in container:
        if item["name"].lower() == product.lower() and item["lot"] < lot:
            return False
    return True


# ---------------------------
# Valida el formato y rango de una fecha
# ---------------------------
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

