import os
import json
from child_classes.functions.validations import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
FILES_DIR = os.path.join(BASE_DIR, "files")

CLIENT_PATH = os.path.join(FILES_DIR, "client.json")
SUPPLIER_PATH = os.path.join(FILES_DIR, "supplier.json")
STOCK_PATH = os.path.join(FILES_DIR, "stock.json")  
SALE_PATH = os.path.join(FILES_DIR, "sale.json")
BUY_PATH = os.path.join(FILES_DIR, "buys.json")


def write_into(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    all_data = return_exist(path)
    all_data.append(data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=4)

def return_exist(path):
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

    while True:
        try:
            ide = int(input("|ID|: "))
            break
        except ValueError:
            print("ID inválido, debe ser un número.")

    name = input("|Nombre        |: ")
    if lock == "cli":
        last = input("|Apellido      |: ")

    while True:
        email = input("|Correo        |: ")
        if "@" in email:
            break
        print("Correo inválido, intente nuevamente.")

    while True:
        try:
            phone = int(input("|Teléfono      |: "))
            break
        except ValueError:
            print("Teléfono inválido, debe ser un número.")

    capsule.append(ide)
    capsule.append(name)
    if lock == "cli":
        capsule.append(last)
    capsule.append(email)
    capsule.append(phone)
    return capsule

def add_stock_func():
    ide = define_id(STOCK_PATH)
    capsule = []

    name = input("|Nombre del producto |: ")

    while True:
        try:
            quantity = int(input("|Cantidad en stock   |: "))
            break
        except ValueError:
            print("Cantidad inválida.")

    while True:
        try:
            price = float(input("|Precio de venta     |: "))
            break
        except ValueError:
            print("Precio inválido.")

    capsule.append(ide)
    capsule.append(name)
    capsule.append(quantity)
    capsule.append(price)
    return capsule

def make_sale_buy(entity):
    global entity_id, date, lot

    ide = define_id(SALE_PATH if entity == "client" else BUY_PATH)
    products = {}
    capsule = []

    while True:
        if entity == "client":
            name_entity = input("|Cliente           |: ")
            valid = validate_exist(CLIENT_PATH, name_entity)
            if valid[0]:
                entity_id = valid[1]
                break
            else:
                print("El cliente no se ha agregado.")
        else:
            name_entity = input("|Proveedor         |: ")
            valid = validate_exist(SUPPLIER_PATH, name_entity)
            if valid[0]:
                entity_id = valid[1]
                break
            else:
                print("El proveedor no se ha agregado.")

    stock_data = return_exist(STOCK_PATH)
    if not stock_data:
        print("\nNo hay productos en el catálogo.\n")
        return

    print("\nCATÁLOGO DE PRODUCTOS DISPONIBLES ")
    print("────────────────────────────────────────────")
    for item in stock_data:
        quantity = item.get("quantity") or item.get("lot") or 0
        price = item.get("sale_price") or item.get("price") or 0
        print(
            f"ID: {item['id']} | {item['name']} - {quantity} unidades disponibles | "
            f"Precio: ${price:,.2f}"
        )
    print("────────────────────────────────────────────\n")

    while True:
        try:
            product_id = int(input("|ID del producto a agregar|: "))
            lot = int(input("|Cantidad a vender|: "))

            product = next((p for p in stock_data if p["id"] == product_id), None)

            if not product:
                print("ID de producto no encontrado. Intente nuevamente.")
                continue

            name_product = product["name"]
            stock_quantity = product.get("quantity") or product.get("lot") or 0

            if entity == "client":
                if lot > stock_quantity:
                    print(
                        f"No hay suficiente stock. Solo hay {stock_quantity} unidades disponibles."
                    )
                    continue

            products[name_product] = lot
            print(f"Producto agregado: {name_product} ({lot} unidades)\n")

            op = input("¿Desea agregar otro producto? (s/n): ").lower()
            if op != "s":
                break

        except ValueError:
            print("Entrada inválida. Debe ingresar números para el ID y la cantidad.\n")
    while True:
        date = input("|Fecha (aaaa-mm-dd)  |: ")
        if valid_date(date):
            break

    capsule.append(ide)
    capsule.append(entity_id)
    capsule.append(products)
    capsule.append(date)

    return capsule

