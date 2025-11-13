import json
import os


def get_file_path(filename):
    """
    Retorna la ruta completa del archivo en la carpeta /files.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, "..", "..", "files", filename)
    return os.path.normpath(file_path)


def define_id(filename):
    """
    Define un nuevo ID incremental para ventas o compras.
    Soporta archivos vacíos o con líneas no válidas.
    """
    path = get_file_path(filename)

    # Asegurar que el archivo exista
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            f.write("")

    with open(path, "r", encoding="utf-8") as file:
        data = file.read().split("\n")

    ide = 1
    dictionary = []

    # Evita errores de JSON en líneas vacías o corruptas
    for key in range(len(data)):
        line = data[key].strip()
        if not line:
            continue
        try:
            dictionary.append(json.loads(line))
        except json.JSONDecodeError:
            continue

    # Buscar IDs existentes
    ids = [item.get("id") for item in dictionary if isinstance(item, dict) and "id" in item]

    if ids:
        while ide in ids:
            ide += 1
    else:
        ide = 1

    return ide


def return_exist(filename):
    """
    Devuelve el contenido del archivo JSON como lista.
    Si el archivo está vacío, devuelve lista vacía.
    """
    path = get_file_path(filename)

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            data = []
    return data


def validate_exist(filename, name):
    """
    Valida si existe una entidad (cliente o proveedor) por nombre.
    Soporta tanto clave 'name' como 'nombre'.
    """
    container = return_exist(filename)
    result = [False, None]

    for item in container:
        item_name = item.get("name") or item.get("nombre")
        if item_name and name.lower() == item_name.lower():
            result[0] = True
            result[1] = item.get("id")
            return result

    return result


def valid_lot(product, lot):
    """
    Valida si el lote ingresado no es menor que los existentes.
    """
    container = return_exist("stocktaking.json")

    for item in container:
        if item["name"].lower() == product.lower() and item["lot"] < lot:
            return False
    return True


def valid_date(date):
    """
    Valida que la fecha tenga formato YYYY-MM-DD y sea lógica.
    """
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
