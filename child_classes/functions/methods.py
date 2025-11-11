import os
import json
from child_classes.functions.validations import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
FILES_DIR = os.path.join(BASE_DIR, "files")

CLIENT_PATH = os.path.join(FILES_DIR, "client.json")
SUPPLIER_PATH = os.path.join(FILES_DIR, "supplier.json")
STOCK_PATH = os.path.join(FILES_DIR, "stocktaking.json")
SALE_PATH = os.path.join(FILES_DIR, "sale.json")
BUY_PATH = os.path.join(FILES_DIR, "buys.json")

def write_into(path, data):
    """Agrega un registro (data) al archivo JSON en la ruta 'path'."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    all_data = return_exist(path)
    all_data.append(data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4)

def return_exist(path):
    """Devuelve la lista de registros desde un archivo JSON, o [] si no existe."""
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def add_entity_func(lock):
    last = None
    email = None
    ide = None
    phone = None
    capsule = []

    i = 1
    while i != 0:
        try:
            ide = int(input("|ID|: "))
            i = 0
        except:
            i = 1

    name = input("|Nombre        |: ")
    if lock == "cli":
        last = input("|Apellido      |: ")

    i = 1
    while i != 0:
        email = input("|Correo        |: ")
        if "@" in email:
            i = 0

    i = 1
    while i != 0:
        try:
            phone = int(input("|Telefono      |: "))
            i = 0
        except:
            i = 1

    capsule.append(ide)
    capsule.append(name)
    if lock == "cli":
        capsule.append(last)
    capsule.append(email)
    capsule.append(phone)
    return capsule

def add_stock_func():
    ide = define_id(STOCK_PATH)
    lot = None
    capsule = []

    name = input("|Nombre    |: ")

    i = 1
    while i != 0:
        try:
            lot = int(input("|Cantidad  |: "))
            i = 0
        except:
            i = 1

    capsule.append(ide)
    capsule.append(name)
    capsule.append(lot)
    return capsule

def make_sale_buy(entity):
    global entity_id, date, lot

    ide = define_id(SALE_PATH if entity == "client" else BUY_PATH)
    product = {}
    capsule = []

    state = True
    state_product = True
    state_date = True

    while state:
        if entity == "client":
            name_entity = input("|Cliente           |: ")
            valid = validate_exist(CLIENT_PATH, name_entity)
            if valid[0]:
                entity_id = valid[1]
                state = False
            else:
                print("El cliente no se ha agregado")
        else:
            name_entity = input("|Proveedor         |: ")
            valid = validate_exist(SUPPLIER_PATH, name_entity)
            if valid[0]:
                entity_id = valid[1]
                state = False
            else:
                print("El proveedor no se ha agregado")

    print("\nPRESIONE 0 PARA DEJAR DE AGREGAR AL CARRITO")
    while state_product:
        val = True
        while val:
            name = input("\n|Producto          |: ")
            valid = validate_exist(STOCK_PATH, name)
            if valid[0]:
                val = False
            else:
                print("El producto no se ha agregado")

        val2 = True
        while val2:
            lot = int(input("|Cantidad          |: "))
            if entity == "client":
                if valid_lot(name, lot):
                    val2 = False
                else:
                    val2 = False
                    print("No hay suficientes productos")
            else:
                val2 = False

        product[name] = lot
        op = int(input("¿Agregar más?: "))
        if op == 0:
            state_product = False

    while state_date:
        date = input("|Fecha aaaa-mm-dd  |: ")
        if valid_date(date):
            state_date = False

    capsule.append(ide)          
    capsule.append(entity_id)    
    capsule.append(product)      
    capsule.append(date)        

    return capsule

