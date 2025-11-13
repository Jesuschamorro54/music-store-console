from parent_classes.facture_class import Facture
from child_classes.functions.validations import *
from child_classes.functions.path_utils import get_file_path
from datetime import datetime


class Sale(Facture):
    def __init__(self):
        super().__init__()
        self.container = None
        self._sale_info = {
            "id": None,
            "client": None,
            "products": {},
            "date": None,
            "total": None,
            }

    @property
    def sale(self):
        return self._sale_info

    @sale.setter
    def sale(self, info):
        self.update_stock(info[2], "sale")
        i = 0
        for key in self._sale_info:
            self._sale_info[key] = info[i]
            i += 1
        file_path = get_file_path("sale.json")
        self.write_into(file_path, self._sale_info)

    def show_range_date(self, date_init, date_final):
        if not valid_date(date_init) or not valid_date(date_final):
            return print("El rango de fecha es invalido")

        file_path = get_file_path("sale.json")
        self.container = return_exist(file_path)

        for i in range(len(self.container)):
            if date_init <= self.container[i]["date"] <= date_final or date_init >= self.container[i]["date"] >= date_final:
                print(f"\033[36m\n-- Detalle de la compra --\033[39m")
                print(f"|ID buy    | -> |{self.container[i]['id']}|")
                print(f"|ID Client | -> |{self.container[i]['client']}|")
                print(f"|Products  |")
                product_list = self.container[i]["products"]
                for key in product_list: print(f"\t\033[31m{key}: {product_list[key]}\033[39m")
                print(f"|Date      | -> |{self.container[i]['date']}|")

    def show_by_id(self, ide):
        file_path = get_file_path("sale.json")
        self.container = return_exist(file_path)
        for i in range(len(self.container)):
            if self.container[i]["id"] == ide:
                print(f"\033[36m\n-- Detalle de la compra --\033[39m")
                print(f"|ID buy    | -> {self.container[i]['id']}")
                print(f"|ID Client | -> {self.container[i]['client']}")
                print(f"|Products  |")
                product_list = self.container[i]["products"]
                for key in product_list: print(f"\t\033[31m{key}: {product_list[key]}\033[39m")
                print(f"|Date      | -> {self.container[i]['date']}")
                return 0
        print("No se encuentra la compra")

    def show_report_date(self, date_init, date_final):
        if not valid_date(date_init) or not valid_date(date_final):
            print("El rango de fecha es inválido")
            return

        sale_path = get_file_path("sale.json")
        client_path = get_file_path("client.json")

        sales = return_exist(sale_path)
        clients = return_exist(client_path)

        client_names = {}
        for c in clients:
            nombre = f"{c['name']} {c['last_name']}"
            client_names[c['id']] = nombre

        ventas_en_rango = []
        for venta in sales:
            if date_init <= venta["date"] <= date_final or date_init >= venta["date"] >= date_final:
                ventas_en_rango.append(venta)

        if not ventas_en_rango:
            print("\nREPORTE DE VENTAS")
            print(f"Del {date_init} al {date_final}")
            print("═════════════════════════════════════════════════════")
            print("No se encontraron ventas en el período indicado.")
            return

        print(f"\nREPORTE DE VENTAS DEL {date_init} AL {date_final}")
        print("════════════════════════════════════════════════════════════")
        print(f"\nVENTAS ENCONTRADAS: {len(ventas_en_rango)} venta(s)")

        print("\n┌─────────────────────────────────────────────────────────┐")
        print("│                    DETALLE DE VENTAS                    │")
        print("└─────────────────────────────────────────────────────────┘")

        total_productos_global = 0

        for idx, venta in enumerate(ventas_en_rango, 1):
            client_id = venta["client"]
            client_name = client_names.get(client_id, "Desconocido")

            print(f"\n Venta #{idx}")
            print(f"   ├── ID Venta: {venta['id']}")
            print(f"   ├── Cliente: {client_name} (ID: {client_id})")
            print(f"   ├── Fecha: {venta['date']}")
            print("   ├── Productos:")

            productos = venta["products"]
            total_productos = 0
            for nombre, cantidad in productos.items():
                print(f"   │   ├── {nombre}: {cantidad} unidades")
                total_productos += cantidad

            print(f"   └── Total de productos: {total_productos}")
            total_productos_global += total_productos

        print("\n┌─────────────────────────────────────────────────────────┐")
        print("│                    RESUMEN GENERAL                      │")
        print("└─────────────────────────────────────────────────────────┘")
        print(f"Total de ventas en el período: {len(ventas_en_rango)}")
        print(f"Total de productos vendidos: {total_productos_global}")
        print(f"Período consultado: {date_init} - {date_final}")


       