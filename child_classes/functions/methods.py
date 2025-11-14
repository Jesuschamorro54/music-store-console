from child_classes.functions.validations import *
from datetime import datetime
import json



# add inventory
def add_stock_func():
    ide = define_id("/Users/NEIDER/Desktop/PROYECTO MUSICA/music-store-console/files/stocktaking.txt")
    lot = None
    capsule = []

    #  Name
    name = input("|Nombre    |: ")

    #  Lot
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
    from datetime import datetime
    from child_classes.functions.validations import validate_exist, define_id

    PRECIOS = {
        "Guitarra Eléctrica": 1500000,
        "Bajo": 1200000,
        "Batería Acústica": 3000000,
        "Ukelele": 250000,
        "Piano Digital": 2000000,
        "Teclado Yamaha": 850000,
        "Micrófono Shure": 450000,
        "Audífonos Pro": 350000,
        "Violín": 900000,
        "Trompeta": 1100000,
        "Partitura": 10000
    }

    path = "files/sale.json" if entity == "client" else "files/buys.json"
    ide = define_id(path)

    productos = []
    productos_dict = {}

    while True:
        if entity == "client":
            name = input("|Cliente           |: ")
            valid = validate_exist("files/client.json", name)
        else:
            try:
                id_entity = int(input("|ID Proveedor     |: "))
            except:
                print("ID inválido.")
                continue
            valid = validate_exist("files/supplier.json", id_entity)

        if id_entity == True:
            print("proveedor encontrado")
        else:
            print ("no existe")

        print("\nPRESIONE 0 PARA DEJAR DE AGREGAR PRODUCTOS")

        while True:
            nombre = input("\n|Producto           |: ").strip().title()
            if nombre == "0":
                break

            if nombre not in PRECIOS:
                print("Producto no existe.")
                continue

            try:
                cantidad = int(input("|Cantidad         |: "))
            except:
                print("Cantidad inválida.")
                continue

            precio = PRECIOS[nombre]
            subtotal = precio * cantidad

            productos_dict[nombre] = {
                "cantidad": cantidad,
                "precio": precio,
                "subtotal": subtotal
            }   

            if input("¿Agregar más productos? (s/n): ").lower() == "n":
                break

        fecha_actual = datetime.now().isoformat()

        return [ide, productos_dict, fecha_actual]

