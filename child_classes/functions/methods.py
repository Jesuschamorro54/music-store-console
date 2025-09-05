from child_classes.functions.validations import *


# add client or supplier
def add_entity_func(lock):
    last = None
    email = None
    ide = None
    phone = None
    capsule = []

    #  Ide
    i = 1
    while i != 0:
        try:
            ide = int(input("|Identificacion|: "))
            i = 0
        except:
            i = 1

    #  Name and lastname
    name = input("|Nombre        |: ")
    if lock == "cli":
        last = input("|Apellido      |: ")
    else:
        pass

    i = 1
    while i != 0:
        email = input("|Correo        |: ")
        for key in range(len(email)):
            if email[key] == "@":
                i = 0
                break

    #  cellphone
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
    else:
        pass
    capsule.append(email)
    capsule.append(phone)
    return capsule


# add inventory
def add_stock_func():
    ide = define_id("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/stocktaking.txt")
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
    ide = define_id("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/sale.txt") if entity == "client" else define_id(
        "/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/buys.txt")
    product = {}
    capsule = []

    state = True
    state_product = True
    state_date = True

    while state:
        if entity == "client":
            name_entity = input("|Cliente           |: ")
            valid = validate_exist("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/client.txt", name_entity)
            if valid[0]:
                entity_id = valid[1]
                state = False
            else:
                print("El cliente no se ha agregado")
        else:
            name_entity = input("|Proveedor         |: ")
            valid = validate_exist("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/supplier.txt", name_entity)
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
            valid = validate_exist("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/stocktaking.txt", name)
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
