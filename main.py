import os

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
        |  1. REGISTRAR CLIENTE   \t\t 6. CONSULTAR VENTAS POR FECHAS  |
        |  2. REGISTRAR PROVEEDOR \t\t 7. CONSULTAR VENTA POR FACTURA  |
        |  3. REGISTRAR VENTA     \t\t 8. CONSULTAR CLIENTE            |
        |  4. REGISTRAR COMPRAS   \t\t 9. CONSULTAR INVENTARIO         |
        |  5. REGISTRAR INVENTARIO\t\t 10.REPORTE DE VENTAS            |
        |  0. salir del sistema\t\t                                         |
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
            data = make_sale_buy("client")
            sale_ins.sale = data

            productos = {"Guitarra": 2, "Batería": 1}
            sale_ins.add_sale(
                id_sale=len(sale_ins.sales) + 1,
                id_cliente=101,
                cliente="Juan Pérez",
                fecha="2025-10-01",
                productos=productos,
            )
            print("\033[32mRegistro exitoso\033[39m")
            input("Presione ENTER para continuar...")

        elif op == "4":
            data = make_sale_buy("supplier")
            buy_ins.buy = data
            print("\033[32mRegistro exitoso\033[39m")
            input("Presione ENTER para continuar...")

        elif op == "5":
            data = add_stock_func()
            stock_ins.stock = data
            print("\033[32mRegistro exitoso\033[39m")
            input("Presione ENTER para continuar...")

        elif op == "6":
            date1 = input("Desde: ")
            date2 = input("Hasta: ")
            sale_ins.show_range_date(date1, date2)
            input("Presione ENTER para continuar...")

        elif op == "7":
            id_sale = input("Ingrese ID: ")
            sale_ins.show_by_id(id_sale)
            input("Presione ENTER para continuar...")

        elif op == "8":
            id_client = int(input("Ingrese ID: "))
            name_client = input("Ingrese nombre: ")
            client_ins.show_client(id_client, name_client)
            input("Presione ENTER para continuar...")

        elif op == "9":
            id_inventory = int(input("Ingrese ID: "))
            stock_ins.show_stock(id_inventory)
            input("Presione ENTER para continuar...")

        elif op == "10":
            date1 = input("Desde (YYYY-MM-DD): ")
            date2 = input("Hasta (YYYY-MM-DD): ")
            sale_ins.show_report(date1, date2)
            input("Presione ENTER para continuar...")

        elif op == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("\033[opción inválida. Intente nuevamente.\033[39m")
            input("Presione ENTER para continuar...")

        clear_screen()