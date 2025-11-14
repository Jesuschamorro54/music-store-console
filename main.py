from child_classes.client_class import Client
from child_classes.sale_class import Sale
from child_classes.stocks import Stock
from child_classes.buys_class import Buy
from child_classes.supplier_class import Supplier
from child_classes.facture import Facture
from child_classes.functions.validations import validate_exist, define_id
from child_classes.functions.methods import make_sale_buy


client_ins = Client()
supplier_ins = Supplier()
stock_ins = Stock()
buy_ins = Buy()
sale_ins = Sale()
facture_ins = Facture()

# ========================= MAIN MENU ==========================
while True:
    op = input(
        """\033[32m
             -- COMPRA Y VENTA DE INSTRUMENTOS MUSICALES --
           \033[39m
    __________________________________________________________________
    -----------------------------| MENU |-----------------------------

    |  1. REGISTRAR CLIENTE        6. CONSULTAR VENTAS POR FECHAS  |
    |  2. REGISTRAR PROVEEDOR      7. CONSULTAR VENTA POR FACTURA  |
    |  3. REGISTRAR VENTA          8. CONSULTAR CLIENTE            |
    |  4. REGISTRAR COMPRAS        9. CONSULTAR INVENTARIO         |
    |                             10. REPORTE DE VENTAS DE FECHA1 A FECHA2 |
    
    Option: """
    )

    # 1. REGISTRAR CLIENTE
    if op == "1":
        data = client_ins.add_entity()
        client_ins.client = data
        print("\033[32mRegistro exitoso\033[39m")
        input()

    # 2. REGISTRAR PROVEEDOR
    elif op == "2":
        data = supplier_ins.add_entity()
        supplier_ins.supplier = data
        print("\033[32mRegistro exitoso\033[39m")
        input()

    # 3. REGISTRAR VENTA
    elif op == "3":
        data = sale_ins.make_sale()
        sale_ins.sale = data
        print("\033[32mRegistro exitoso\033[39m")
        input()

    # 4. REGISTRAR COMPRA (Usando Facture)
    elif op == "4":
        print("\n=== FACTURA MÁS RECIENTE ===")
        ultima = facture_ins.load_last()

        if ultima:
            facture_ins.show(ultima)
            cont = input("¿Registrar nueva compra? (s/n): ").lower()
            if cont != "s":
                input()
                continue
        supplier_id = input("Ingrese ID del proveedor: ")


        data = make_sale_buy ("supplier")

        factura_id = data[0]
        productos = data[1]
        fecha = data[2]


        # Normalizar productos
        lista_productos = []
        for nombre, info in productos.items():
            qty = info["cantidad"]
            price = info["precio"]
            subtotal = qty * price

            lista_productos.append({
                "name": nombre,
                "quantity": qty,
                "price": price,
                "subtotal": subtotal
            })

        total = sum(p["subtotal"] for p in lista_productos)

        factura = {
            "factura_id": factura_id,
            
            "products": lista_productos,
            "total": total,
            "fecha": fecha
        }

        # Guardar factura
        Facture.write_into("files/factura.json", factura)

        # Guardar compra
        buy_ins.buy = data

        # Actualizar inventario
        facture_ins.update_stock(productos, mode="buy")

        print("\n\033[32mCompra registrada exitosamente.\033[39m\n")
        input()

    # 6. CONSULTAR VENTAS POR FECHA
    elif op == "6":
        date1 = input("Desde: ")
        date2 = input("Hasta: ")
        sale_ins.show_range_date(date1, date2)
        input()

    # 7. CONSULTAR VENTA POR FACTURA
    elif op == "7":
        try:
            id_sale = int(input("Ingrese ID: "))
            sale_ins.show_by_id(id_sale)
        except Exception:
            print("ID inválido")
        input()

    # 8. CONSULTAR CLIENTE
    elif op == "8":
        try:
            id_client = int(input("Ingrese ID: "))
            name_client = input("Ingrese nombre: ")
            client_ins.show_client(id_client, name_client)
        except Exception:
            print("ID inválido")
        input()

    # 9. CONSULTAR INVENTARIO
    elif op == "9":
        inventory = [
            "Saxofon: ID 1",
            "Corno: ID 2",
            "Flauta: ID 3",
            "Clarinete: ID 10",
            "Trombon: ID 11",
            "Trompeta: ID 12"
        ]
        print("Consultar por ID")
        print(inventory)
        try:
            id_inventory = int(input("Ingrese ID: "))
            stock_ins.show_stock(id_inventory)
        except Exception:
            print("ID inválido")
        input()

    #  SALIR
    elif op == "0":
        exit()
