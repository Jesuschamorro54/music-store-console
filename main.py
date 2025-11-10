import os
import json
import datetime

from child_classes.client_class import *
from child_classes.sale_class import *
from child_classes.stocks import *
from child_classes.buys_class import *
from child_classes.supplier_class import *
from child_classes.functions.methods import (
    add_entity_func,
    make_sale_buy,
    add_stock_func,
)




# Instancias globales
client_ins = Client()
supplier_ins = Supplier()
stock_ins = StockManager()
buy_ins = Buy()
sale_ins = Sale()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == '__main__':
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
        |  5. REGISTRAR INVENTARIO\t\t 10.REPORTE DE VENTAS            |
        |  0. salir del sistema   \t\t                                 |
        Option: """
        )

        clear_screen()

        if op == "1":
            data = add_entity_func("cli")
            client_ins.client = data
            print("\033[32mRegistro exitoso\033[39m")
            input("Presione ENTER para continuar...")

        elif op == "2":
            data = add_entity_func("supp")
            supplier_ins.supplier = data
            print("\033[32mRegistro exitoso\033[39m")
            input("Presione ENTER para continuar...")

        elif op == "3":
            data = add_entity_func("sale")
            sale_ins.sale = data
            print("\033[32mRegistro exitoso\033[39m")
            input("Presione ENTER para continuar...")

        elif op == "4":
           data = add_entity_func("buy")
           buy_ins.buy = data
           print("\033[32mRegistro exitoso\033[39m")
           input("Presione ENTER para continuar...")
           
        elif op == "5":
            print("opcion no valida en este momento...")

        elif op == "6":
            d1 = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
            d2 = input("Ingrese la fecha final (YYYY-MM-DD): ")
            sale_ins.show_range_date(d1, d2)
            input("Presione ENTER para continuar...")

        elif op == "7":
            id_sale = input("Ingrese el ID de la venta: ")
            sale_ins.show_by_id(id_sale)
            input("Presione ENTER para continuar...")

        #  CONSULTAR CLIENTE
        elif op == "8":
           id_client = int(input("Ingrese ID: "))
           print(client_ins.show_client(id_client, ""))


        elif op == "9":
            stock_ins.show_stock()
            input("Presione ENTER para continuar...")

        elif op == "10":
            print("\nREPORTE DE VENTAS")
            d1 = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
            d2 = input("Ingrese la fecha final (YYYY-MM-DD): ")
            sale_ins.report_sales_from_json(d1, d2)
            input("Presione ENTER para continuar...")

        elif op == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione ENTER para continuar...")

