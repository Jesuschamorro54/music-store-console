import json
import os


def define_id(path):
    """Devuelve el siguiente ID disponible en el archivo JSONL."""
    if not os.path.exists(path) or os.stat(path).st_size == 0:
        return 1

    with open(path, "r") as file:
        data = file.read().strip().split("\n")

    dictionary = [json.loads(line) for line in data if line.strip()]
    ids = [item["id"] for item in dictionary]

    ide = 1
    while ide in ids:
        ide += 1
    return ide


def return_exist(path):
    """Devuelve todos los registros de un archivo JSONL como lista de dicts."""
    if not os.path.exists(path) or os.stat(path).st_size == 0:
        return []

    with open(path, "r") as file:
        data = file.read().strip().split("\n")

    return [json.loads(line) for line in data if line.strip()]


def validate_exist(path, name):
    """Verifica si existe una entidad por nombre (case-insensitive)."""
    container = return_exist(path)
    for item in container:
        if name.lower() == item["name"].lower():
            return [True, item["id"]]
    return [False, None]


def valid_lot(product, lot):
    """Verifica que haya suficiente stock del producto solicitado."""
    container = return_exist(
        "child_classes/files/stocktaking.txt"
    )
    for item in container:
        if item["name"].lower() == product.lower():
            return item["lot"] >= lot
    return False


def valid_date(date):
    """Valida que la fecha esté en formato YYYY-MM-DD y dentro de rango aceptable."""
    if not date or len(date) != 10:
        print("Invalid date")
        return False

    try:
        year, month, day = map(int, date.split("-"))
    except ValueError:
        print("Invalid format")
        return False

    if not (1 <= day <= 31):
        print("Invalid day")
        return False
    if not (1 <= month <= 12):
        print("Invalid month")
        return False
    if not (2000 <= year <= 2025):
        print("Invalid year")
        return False

    return True
