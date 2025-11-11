from parent_classes.facture_class import Facture
from child_classes.functions.validations import *
import datetime
import json
import os

class Sale(Facture):
    def __init__(self):
        super().__init__()
        self.container = None
        self._sale_info = {
            "ID": None,
            "Cliente": None,
            "Products": {},
            "Date": None,
        }

    @property
    def sale(self):
        return self._sale_info

    @sale.setter
    def sale(self, info):
        from datetime import datetime

        self.update_stock(info[2], "sale")

        self._sale_info["id"] = info[0]
        self._sale_info["client"] = info[1]
        self._sale_info["products"] = info[2]
        self._sale_info["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.write_into(
            "C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/sale.json",
            self._sale_info
        )

    def show_range_date(self, date_init, date_final):
        if not valid_date(date_init) or not valid_date(date_final):
            return print("El rango de fecha es inválido")

        self.container = return_exist("C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/sale.json")
        ventas_en_rango = []
        for venta in self.container:
            fecha = venta.get("date")
            if fecha and (date_init <= fecha <= date_final or date_init >= fecha >= date_final):
                ventas_en_rango.append(venta)

        stock_file = "C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/stock.json"
        stock_data = return_exist(stock_file)
        stock_dict = {item["name"].lower(): item.get("sale_price", 0) for item in stock_data}

        total_productos = 0
        total_monetario = 0
        cantidad_ventas = len(ventas_en_rango)

        print(f"\nREPORTE DE VENTAS DEL {date_init} AL {date_final}")
        print("════════════════════════════════════════════════════════════")
        print(f"\nVENTAS ENCONTRADAS: {cantidad_ventas} venta(s)\n")
        print("┌─────────────────────────────────────────────────────────┐")
        print("│                    DETALLE DE VENTAS                    │")
        print("└─────────────────────────────────────────────────────────┘\n")

        for idx, venta in enumerate(ventas_en_rango, start=1):
            suma_venta = 0
            subtotal_monetario = 0
            print(f"Venta #{idx}")
            print(f"   ├── ID Venta: {venta['id']}")
            print(f"   ├── Cliente: {venta['client']} (ID: {venta['id']})")
            print(f"   ├── Fecha: {venta['date']}")
            print(f"   ├── Productos:")
            for nombre, cantidad in venta["products"].items():
                precio = stock_dict.get(nombre.lower(), 0)
                subtotal = cantidad * precio
                print(f"   │   ├── {nombre}: {cantidad} unidades x ${precio:,.2f} = ${subtotal:,.2f}")
                try:
                    suma_venta += int(cantidad)
                except:
                    suma_venta += 0
                subtotal_monetario += subtotal
            print(f"   └── Total de productos: {suma_venta}")
            print(f"   └── Subtotal monetario: ${subtotal_monetario:,.2f}\n")

            total_productos += suma_venta
            total_monetario += subtotal_monetario

        print("┌─────────────────────────────────────────────────────────┐")
        print("│                    RESUMEN GENERAL                      │")
        print("└─────────────────────────────────────────────────────────┘\n")
        print(f"Total de ventas en el período: {cantidad_ventas}")
        print(f"Total de productos vendidos: {total_productos}")
        print(f"Total monetario de todas las ventas: ${total_monetario:,.2f}")
        print(f"Período consultado: {date_init} - {date_final}")

    def show_by_id(self, ide):
        self.container = return_exist("C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/sale.json")
        for venta in self.container:
            if venta["id"] == ide:
                print(f"\033[36m\n-- Detalle de la compra --\033[39m")
                print(f"|ID Venta   | -> {venta['id']}")
                print(f"|Cliente    | -> {venta['client']}")
                print("|Productos  |")
                for nombre, cantidad in venta["products"].items():
                    print(f"  - {nombre}: {cantidad}")
                print(f"|Fecha      | -> {venta['date']}")
                return
        print("No se encuentra la compra")

