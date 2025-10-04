#  from Parcial_III.child_classes.functions.methods import *
from child_classes.client_class import *
from child_classes.sale_class import *
import json
from datetime import datetime
from child_classes.stocks import *
from child_classes.buys_class import *
from child_classes.supplier_class import *


client_ins = Client()
supplier_ins = Supplier()
stock_ins = Stock()
buy_ins = Buy()
sale_ins = Sale()

# Init the appplication
while True:
    
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
    |  5. REGISTRAR INVENTARIO\t\t 10. REPORTE DE VENTAS DE FECHA1 A FECHA2                      |
    
    Option: """
    )



    #  REGISTRAR CLIENTE
    if op == "1":
        data = add_entity_func("cli")
        client_ins.client = data  # Call the method setter
        print("\033[32mRegistro exitoso\033[39m")
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

    #  REGISTRAR INVENTARIO
    elif op == "5":
        data = add_stock_func()
        stock_ins.stock = data
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

    #  CONSULTAR INVENTARIO
    elif op == "9":

        inventory = ["Saxofon: ID 1", "Corno: ID 2", "Flauta: ID 3", "Clarinete: ID 10", "Trombon: ID 11", "Trompeta: ID 12"]
        print ("Consultar por ID")
        print (inventory)
     

        id_inventory = int(input("Ingrese ID: "))
        stock_ins.show_stock(id_inventory)
        input()

    elif op == "10":
        # Pedimos rango
        fecha_inicio = input("Desde (YYYY-MM-DD): ").strip()
        fecha_fin = input("Hasta (YYYY-MM-DD): ").strip()

        # Validamos formato de fechas
        try:
            d1 = datetime.strptime(fecha_inicio, "%Y-%m-%d")
            d2 = datetime.strptime(fecha_fin, "%Y-%m-%d")
        except Exception:
            print("Formato de fecha inválido. Usa YYYY-MM-DD.")
            input()
            continue

        # Leemos archivo de ventas
        try:
            f = open("files/sale.txt", "r")
            ventas = f.readlines()
            f.close()
        except FileNotFoundError:
            print("No se encontró el archivo files/sale.txt")
            input()
            continue

        print("\n--- VENTAS EN EL RANGO ---\n")
        encontrado = False

        for linea in ventas:
            linea = linea.strip()
            if not linea:
                continue
            try:
                venta = json.loads(linea)
            except Exception:
                # si la línea está mal formada la saltamos
                continue

            fecha_text = venta.get("date", "")
            try:
                fecha_venta = datetime.strptime(fecha_text, "%Y-%m-%d")
            except Exception:
                continue

            # Inclusivo: incluye fecha_inicio y fecha_fin
            if d1 <= fecha_venta <= d2:
                print("ID:", venta.get("id"),
                      "Cliente:", venta.get("client"),
                      "Productos:", venta.get("products"),
                      "Fecha:", fecha_text)
                encontrado = True

        if not encontrado:
            print("No se encontraron ventas en ese rango.")

        input()  # pausa antes de las consultas siguientes

        # --- Consultas opcionales (puedes dejar vacío para omitir) ---
        venta_id_str = input("Ingresa ID de venta (enter para omitir): ").strip()
        if venta_id_str:
            try:
                venta_id = int(venta_id_str)
                sale_ins.show_by_id(venta_id)
            except Exception:
                print("ID de venta inválido.")
            input()

        cliente_id_str = input("Ingresa ID de cliente (enter para omitir): ").strip()
        if cliente_id_str:
            try:
                cliente_id = int(cliente_id_str)
                nombre_cliente = input("Ingresa nombre de cliente: ")
                client_ins.show_client(cliente_id, nombre_cliente)
            except Exception:
                print("ID de cliente inválido.")
            input()

        producto_id_str = input("Ingresa ID de producto (enter para omitir): ").strip()
        if producto_id_str:
            try:
                producto_id = int(producto_id_str)
                stock_ins.show_stock(producto_id)
            except Exception:
                print("ID de producto inválido.")
            input()


    elif op == "0":
        exit()