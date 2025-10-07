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
stock_ins = Stock()
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
        |  1. REGISTRAR CLIENTE    \t\t 6. CONSULTAR VENTAS POR FECHAS |
        |  2. REGISTRAR PROVEEDOR \t\t 7. CONSULTAR VENTA POR FACTURA  |
        |  3. REGISTRAR VENTA     \t\t 8. CONSULTAR CLIENTE            |
        |  4. REGISTRAR COMPRAS   \t\t 9. CONSULTAR INVENTARIO         |
        |  5. REGISTRAR INVENTARIO\t\t 10.REPORTE DE VENTAS            |
        |  0. salir del sistema\t\t                                    |
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
            make_sale_buy("sale", sale_ins, client_ins)

        elif op == "4":
            make_sale_buy("buy", buy_ins, supplier_ins)

        elif op == "5":
            add_stock_func(stock_ins)

        elif op == "6":
            d1 = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
            d2 = input("Ingrese la fecha final (YYYY-MM-DD): ")
            sale_ins.show_range_date(d1, d2)
            input("Presione ENTER para continuar...")

        elif op == "7":
            id_sale = input("Ingrese el ID de la venta: ")
            sale_ins.show_by_id(id_sale)
            input("Presione ENTER para continuar...")

        elif op == "8":
            client_ins.show_clients()
            input("Presione ENTER para continuar...")

        elif op == "9":
            stock_ins.show_stocks()
            input("Presione ENTER para continuar...")

        elif op == "10":
            print("\n📊 REPORTE DE VENTAS (desde files/sale.txt)")
            d1 = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
            d2 = input("Ingrese la fecha final (YYYY-MM-DD): ")
            sale_ins.report_sales_from_txt(d1, d2)
            input("Presione ENTER para continuar...")

        elif op == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione ENTER para continuar...")

