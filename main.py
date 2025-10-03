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


def parse_date(fecha):
    """Intenta convertir `fecha` a datetime.date."""
    if isinstance(fecha, datetime.date):
        return fecha
    if not isinstance(fecha, str):
        raise ValueError("Fecha debe ser string o datetime.date")

    fecha = fecha.strip()
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.datetime.strptime(fecha, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha no reconocido: {fecha!r}. Use YYYY-MM-DD")


class Sale:
    def __init__(self):
        self.file_path = "files/sale.json"
        self.sales = []

        # cargar archivo si existe
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    # convertir fechas a datetime
                    for venta in data:
                        venta["fecha"] = parse_date(venta["fecha"])
                    self.sales = data
                except json.JSONDecodeError:
                    self.sales = []

    def _save_to_file(self):
        # convertir fechas a string antes de guardar
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(
                [
                    {**venta, "fecha": venta["fecha"].isoformat()}
                    for venta in self.sales
                ],
                f,
                indent=4,
                ensure_ascii=False
            )

    def add_sale(self, id_sale, id_cliente, cliente, fecha, productos):
        fecha_obj = parse_date(fecha)
        productos_normalizados = {
            k: int(v) if str(v).isdigit() else 0
            for k, v in (productos or {}).items()
        }
        nueva_venta = {
            "id": id_sale,
            "id_cliente": id_cliente,
            "cliente": cliente,
            "fecha": fecha_obj,
            "productos": productos_normalizados,
        }
        self.sales.append(nueva_venta)
        self._save_to_file()

    def _format_fecha(self, fecha_val):
        try:
            if isinstance(fecha_val, datetime.date):
                return fecha_val.isoformat()
            return parse_date(str(fecha_val)).isoformat()
        except Exception:
            return str(fecha_val)

    def show_report(self, date1, date2):
        try:
            start = parse_date(date1)
            end = parse_date(date2)
        except ValueError as e:
            print("Error en fechas:", e)
            return

        if start > end:
            print("La fecha 'Desde' no puede ser mayor que 'Hasta'.")
            return

        print(f"\n📊 REPORTE DE VENTAS SOLICITADAS DEL {start.isoformat()} AL {end.isoformat()}")
        print("════════════════════════════════════════════════════════════")

        ventas_filtradas = [
            venta for venta in self.sales
            if start <= parse_date(venta["fecha"]) <= end
        ]

        print(f"\n🔍 VENTAS HALLADAS: {len(ventas_filtradas)} venta(s)\n")

        total_productos = 0
        for idx, venta in enumerate(ventas_filtradas, start=1):
            print(f"📋 Venta #{idx}")
            print(f"   ├── ID Venta: {venta['id']}")
            print(f"   ├── Cliente: {venta['cliente']} (ID: {venta['id_cliente']})")
            print(f"   ├── Fecha: {self._format_fecha(venta['fecha'])}")
            print("   ├── Productos:")
            suma_venta = 0
            for prod, cant in venta["productos"].items():
                print(f"   │   ├── {prod}: {cant} unidades")
                suma_venta += cant
            total_productos += suma_venta
            print(f"   └── Total de productos: {suma_venta}\n")

        print("┌─────────────────────────────────────────────────────────┐")
        print("│                    RESUMEN GENERAL                      │")
        print("└─────────────────────────────────────────────────────────┘\n")

        print(f"💰 Total de ventas en el período: {len(ventas_filtradas)}")
        print(f"📦 Total de productos vendidos en el período: {total_productos}")
        print(f"📅 Período consultado: {start.isoformat()} - {end.isoformat()}\n")

    def show_range_date(self, date1, date2):
        self.show_report(date1, date2)

    def show_by_id(self, id_sale):
        try:
            id_sale = int(id_sale)
        except Exception:
            print("ID inválido. Debe ser un número.")
            return

        venta = next((v for v in self.sales if v["id"] == id_sale), None)
        if not venta:
            print(f"No se encontró venta con ID {id_sale}.")
            return

        print("┌─────────────────────────────────────────────────────────┐")
        print(f"│                    VENTA ID {id_sale}                  │")
        print("└─────────────────────────────────────────────────────────┘\n")
        print(f"ID Venta: {venta['id']}")
        print(f"Cliente: {venta['cliente']} (ID: {venta['id_cliente']})")
        print(f"Fecha: {self._format_fecha(venta.get('fecha'))}")
        print("Productos:")
        for prod, cant in venta['productos'].items():
            print(f" - {prod}: {cant} unidades")
        print("\n")


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
            print("\033[31mOpción inválida. Intente nuevamente.\033[39m")
            input("Presione ENTER para continuar...")

        clear_screen()