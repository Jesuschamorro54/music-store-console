from child_classes.functions.validations import *
from child_classes.functions.path_utils import get_file_path


# add inventory
def add_stock_func():
    file_path = get_file_path("stocktaking.json")
    ide = define_id(file_path)
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
    sale_file_path = get_file_path("sale.json")
    buys_file_path = get_file_path("buys.json")
    ide = define_id(sale_file_path) if entity == "client" else define_id(buys_file_path)
    product = {}
    capsule = []

    state = True
    state_product = True
    state_date = True

    while state:
        if entity == "client":
            name_entity = input("|Cliente           |: ")
            client_file_path = get_file_path("client.json")
            valid = validate_exist(client_file_path, name_entity)
            if valid[0]:
                entity_id = valid[1]
                state = False
            else:
                print("El cliente no se ha agregado")
        else:
            name_entity = input("|Proveedor         |: ")
            supplier_file_path = get_file_path("supplier.json")
            valid = validate_exist(supplier_file_path, name_entity)
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
            stock_file_path = get_file_path("stocktaking.json")
            valid = validate_exist(stock_file_path, name)
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

        product[name] = lot
        op = int(input("¿Agregar más?: "))
        if op == 0: state_product = False

    while state_date:
        date = input("|Fecha aaaa-mm-dd  |: ")
        if valid_date(date): state_date = False

    capsule.append(ide) # 0
    capsule.append(entity_id) # 1
    capsule.append(product) # 2
    capsule.append(date)
    return capsule
