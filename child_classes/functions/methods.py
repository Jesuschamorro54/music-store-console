from child_classes.functions.validations import *
from datetime import datetime



# add inventory
def add_stock_func():
    ide = define_id("/poo/music-store-console/files/stocktaking.txt")
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
    global entity_id, date, lot
    ide = define_id("/poo/music-store-console/files/sale.json") if entity == "client" else define_id(
        "/poo/music-store-console/files/buys.json")
    product = {}
    capsule = []

    state = True
    state_product = True
    state_date = True

    while state:
        if entity == "client":
            name_entity = input("|Cliente           |: ")
            valid = validate_exist("/poo/music-store-console/files/client.json", name_entity)
            if valid[0]:
                entity_id = valid[1]
                state = False
            else:
                print("El cliente no se ha agregado")
        else:
            id_entity = int(input("|ID Proveedor     |: "))
            print(f"proveedor con id {id_entity} encontrado")
           
            valid = validate_exist("/poo/music-store-console/files/supplier.json", id_entity)
            if valid[0]:
                entity_id = valid[1]
                state = False
            else:
                print("El proveedor no se ha agregado")

    print("\nPRESIONE 0 PARA DEJAR DE AGREGAR AL CARRITO")
    while state_product:
        global name
        val = True
        while val:
            name = (input("\n|Producto          |: "))
            valid = validate_exist("/poo/music-store-console/files/stocktaking.json", name)
            if valid[0]:
                val = False
            else:
                print("El producto no se ha agregado")
        val2 = True
        while val2:
            lot = int(input("|Cantidad          |:"))
            if entity == "client":
                if valid_lot(name, lot):
                    val2 = False
                else:
                    val2 = False, print("No hay suficientes productos")
            else:
                val2 = False

#no dejaba seguir agregando productos, agregue una opcion mas para la confirmacion de agregar productos
        product[name] = lot
        op = int(input("¿Agregar más? elija 0 para no o 1 para sí: "))
        if op == 0:state_product = False
        if op == 1: state_product = True

    fecha_actual = datetime.now()
    print(fecha_actual)

    capsule.append(ide) # 0
    capsule.append(entity_id) # 1
    capsule.append(product) # 2
    capsule.append(fecha_actual)
    return capsule
