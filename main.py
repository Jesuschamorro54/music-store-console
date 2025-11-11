import os
from child_classes.client_class import *
from child_classes.sale_class import *
from child_classes.stocks import *
from child_classes.buys_class import *
from child_classes.supplier_class import *
from child_classes.functions.methods import make_sale_buy

client_ins = Client()
supplier_ins = Supplier()
stock_ins = StockManager()
buy_ins = Buy()
sale_ins = Sale()

def clear_screen():
    """Limpia la consola (Windows/Linux/Mac)."""
    os.system("cls" if os.name == "nt" else "clear")

while True:
    op = input(
        """\033[32m
             -- COMPRA Y VENTA DE INSTRUMENTOS MUSICALES --
           \033[39m
    __________________________________________________________________
    -----------------------------| MENU |-----------------------------
        
    |  1. REGISTRAR CLIENTE    \t\t 6.  CONSULTAR VENTAS POR FECHAS  |
    |  2. REGISTRAR PROVEEDOR  \t\t 7.  CONSULTAR VENTA POR FACTURA  |
    |  3. REGISTRAR VENTA      \t\t 8.  CONSULTAR CLIENTE            |
    |  4. REGISTRAR COMPRAS    \t\t 9.  CONSULTAR INVENTARIO         |
    |  5. AGREGAR INVENTARIO   \t\t 10. REPORTES DE VENTAS           |
    |  0. SALIR                \t\t                                  |
    
    Option: """
    )

    clear_screen()

    if op == "1":
        print("\n--- Registro de Cliente ---")
        client_ins = Client()
        data = []
        for campo in client_ins.client.keys():
            valor = input(f"Ingrese {campo}: ").strip()
            data.append(valor)
        client_ins.client = data
        print("\n\033[32m✓ Cliente registrado exitosamente\033[39m")
        input("Presione ENTER para continuar...")

    elif op == "2":
        print("\nREGISTRO DE PROVEEDOR")
        print("═══════════════════════════")
        supplier_ins = Supplier()
        data = []
        for campo in supplier_ins.supplier.keys():
            valor = input(f"Ingrese {campo}: ").strip()
            data.append(valor)
        supplier_ins.supplier = data
        print("\n\033[32m✓ Proveedor registrado exitosamente\033[39m")
        input("Presione ENTER para continuar...")

    elif op == "3":
        data = make_sale_buy("client")
        if data: 
            sale_ins.sale = data
        input("\nPresione ENTER para continuar...")
    
    elif op == "4":
        data = make_sale_buy("supplier")
        if data:  
            buy_ins.buy = data
            print("\n\033[32m✓ Compra registrada exitosamente\033[39m")
        input("\nPresione ENTER para continuar...")

    elif op == "5":
        print("\033[31mOpción inválida. Intente nuevamente cuando este activa...\033[39m")
        input("Presione ENTER para continuar...")
   
    elif op == "6":
        date1 = input("Desde: ")
        date2 = input("Hasta: ")
        sale_ins.show_range_date(date1, date2)
        input("Presione ENTER para continuar...")


    elif op == "7":
        id_sale = int(input("Ingrese ID: "))
        sale_ins.show_by_id(id_sale)
        input("Presione ENTER para continuar...")
    
    elif op == "8":
        id_client = int(input("Ingrese ID: "))
        client_ins.show_client(id_client,)
        input("Presione ENTER para continuar...")
   
    elif op == "9":
        stock_ins.show_stock()
        input("Presione ENTER para continuar...")

    elif op == "10":
        date1 = input("Desde: ")
        date2 = input("Hasta: ")
        sale_ins.show_range_date(date1, date2)
        input("Presione ENTER para continuar...")

    elif op == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("\033[Opción inválida. Intente nuevamente.\033[39m")
        input("Presione ENTER para continuar...")

    clear_screen()  
