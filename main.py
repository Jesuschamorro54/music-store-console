#  from Parcial_III.child_classes.functions.methods import *
from child_classes.client_class import *
from child_classes.sale_class import *
from child_classes.stocks import *
from child_classes.buys_class import *
from child_classes.supplier_class import *

import json
from datetime import datetime
from child_classes.path_manager import get_file_path
# 

client_ins = Client()
supplier_ins = Supplier()
stock_ins = Stock()
buy_ins = Buy()
sale_ins = Sale()



# Init the appplication
while True:
   # pyautogui.click(x=-926, y=525)

   # pyautogui.hotkey('Ctrl', 'l')
    op = input(
        """\033[32m
             -- COMPRA Y VENTA DE INSTRUMENTOS MUSICALES --
           \033[39m
    __________________________________________________________________
    -----------------------------| MENU |-----------------------------
        
    |  1. REGISTRAR CLIENTE   \t\t 6. CONSULTAR VENTAS POR FECHAS  |
    |  2. REGISTRAR PROVEEDOR \t\t 7. CONSULTAR VENTA POR FACTURA  |
    |  3. REGISTRAR VENTA     \t\t 8. CONSULTAR CLIENTE            |
    |  4. REGISTRAR COMPRAS   \t\t 9. CONSULTAR INVENTARIO         |
    |                         \t\t 10. CONSULTAR DE VENTAS         |
    |  0. SALIR
    
    Option: """

    )
    
#jijijja
  #  pyautogui.click(x=-926, y=525)
  #  pyautogui.hotkey('Ctrl', 'l')

    #  REGISTRAR CLIENTE
    if op == "1":
        data = add_entity_func("cli")
        client_ins.client = data  # Call the method setter
        print("\033[32mRegistro exitoso, se Ah guardado correctamente los datos en el archivo del Client\033[39m")
        input()

    #  REGISTRAR PROVEEDOR
    elif op == "2":
        data = add_entity_func("supp")
        supplier_ins.supplier = data
        print("\033[32mRegistro exitoso\033[39m")
        input()

    #  REGISTRAR VENTA
    elif op == "3":
        data = make_sale_buy("client")
        sale_ins.sale = data
        print("\033[32mRegistro exitoso\033[39m")
        input()

    #  REGISTRAR COMPRAS
    elif op == "4":
        data = make_sale_buy("supplier")
        buy_ins.buy = data
        print("\033[32mRegistro exitoso\033[39m")
        input()

    #  CONSULTAR VENTA POR FECHA
    elif op == "6":
        date1 = input("Desde: ")
        date2 = input("Hasta: ")
        sale_ins.show_range_date(date1, date2)
        input()

    #  CONSULTAR VENTA POR FACTURA
    elif op == "7":
        id_sale = int(input("Ingrese ID: "))
        sale_ins.show_by_id(id_sale)
        input()

    #  CONSULTAR CLIENTE
    elif op == "8":
        id_client = int(input("Ingrese ID: "))
        name_client = input("Ingrese nombre: ")
        client_ins.show_client(id_client, name_client)
        input()

    elif op == "9":
            date1 = input("Desde: ")
            date2 = input("Hasta: ")
            sale_ins.show_range_date(date1, date2)
            input()
            id_sale = int(input("Ingrese ID de venta: "))
            sale_ins.show_by_id(id_sale)
            input()
            id_client = int(input("Ingrese ID de cliente: "))
            name_client = input("Ingrese nombre de cliente: ")
            client_ins.show_client(id_client, name_client)
            input()
            id_inventory = int(input("Ingrese ID de producto: "))
            stock_ins.show_stock(id_inventory)
            input()

#  CONSULTA LAS VENTAS EN UN PERIODO DE TIEMPO ESPECIFICO
    elif op == "10":
        primer_parametro = input("Desde (YYYY-MM-DD): ")
        segundo_parametro = input("Hasta (YYYY-MM-DD): ")

        file_path = get_file_path("sale.json") # direccion del archivo de compras, tipo json

        # Cargar el JSON como lista de ventas
        with open(file_path, "r") as f:
            ventas = json.load(f) # de acuerdo al estilo de extructuras

        print("\n--- VENTAS EN EL RANGO ESTIPULADO POR EL CLIENTE/ADMINISTRADOR---\n")
        encontrado = False

        for venta in ventas:
            fecha = venta["date"]

            if primer_parametro <= fecha <= segundo_parametro:
                print("ID:", venta["id"], 
                    "Cliente/Proveedor:", venta.get("client", venta.get("supplier", "???")),
                    "Productos:", venta["products"],
                    "Fecha:", venta["date"])
                encontrado = True

        if not encontrado:
            print("No se encontraron ventas en ese rango.")

        input()


    else:   "0"
    exit()