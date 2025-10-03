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
    """Convierte una cadena o fecha a datetime.date. Permite 'YYYY-MM-DD', 'DD-MM-YYYY', 'DD/MM/YYYY'."""
    if isinstance(fecha, datetime.date):
        return fecha
    if isinstance(fecha, datetime.datetime):
        return fecha.date()
    if not isinstance(fecha, str):
        raise ValueError("Fecha debe ser string o datetime.date")
    fecha = fecha.strip()
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.datetime.strptime(fecha, fmt).date()
        except ValueError:
            continue
    raise ValueError(f"Formato de fecha no reconocido: {fecha!r}. Use YYYY-MM-DD")


def report_sales_from_txt(date1, date2, sale_file_path=None):
    """
    Lee files/sale.txt (cada línea es un JSON) y muestra las ventas entre date1 y date2 (inclusive).
    """
    try:
        start = parse_date(date1)
        end = parse_date(date2)
    except ValueError as e:
        print("Error en fechas:", e)
        return

    if start > end:
        print("La fecha 'Desde' no puede ser mayor que 'Hasta'.")
        return

    if sale_file_path is None:
        base = os.path.dirname(os.path.abspath(__file__))
        sale_file_path = os.path.join(base, "files", "sale.txt")

    if not os.path.exists(sale_file_path):
        print(f"No se encontró el archivo de ventas en: {sale_file_path}")
        return

    ventas = []
    with open(sale_file_path, "r", encoding="utf-8", errors="ignore") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            try:
                obj = json.loads(ln)
            except Exception:
                print("Advertencia: línea de ventas inválida (se omite):", ln[:120])
                continue

            # Normalizar campos
            date_str = obj.get("date") or obj.get("fecha")
            try:
                date_obj = parse_date(date_str)
            except Exception:
                print("Advertencia: fecha inválida en línea (se omite):", ln[:120])
                continue

            ventas.append({
                "id": obj.get("id"),
                "client": obj.get("client") or obj.get("cliente"),
                "date": date_obj,
                "products": obj.get("products") or obj.get("productos") or {},
            })

    ventas_filtradas = [v for v in ventas if start <= v["date"] <= end]

    print(f"\n📊 REPORTE DE VENTAS DESDE {start.isoformat()} HASTA {end.isoformat()}")
    print("════════════════════════════════════════════════════════════\n")
    if not ventas_filtradas:
        print("No se encontraron ventas en el rango indicado.\n")
        return

    total_productos = 0
    for i, venta in enumerate(ventas_filtradas, start=1):
        print(f"📋 Venta #{i}")
        print(f"   ├── ID Venta: {venta.get('id')}")
        print(f"   ├── Cliente: {venta.get('client')}")
        print(f"   ├── Fecha: {venta.get('date').isoformat()}")
        print("   ├── Productos:")
        suma_venta = 0
        for prod, cant in (venta.get("products") or {}).items():
            try:
                cantidad = int(cant)
            except Exception:
                try:
                    cantidad = int(str(cant).strip())
                except Exception:
                    cantidad = 0
            print(f"   │   ├── {prod}: {cantidad} unidades")
            suma_venta += cantidad
        total_productos += suma_venta
        print(f"   └── Total de productos (esta venta): {suma_venta}\n")

    print("┌─────────────────────────────────────────────────────────┐")
    print("│                    RESUMEN GENERAL                      │")
    print("└─────────────────────────────────────────────────────────┘\n")
    print(f"💰 Total de ventas en el período: {len(ventas_filtradas)}")
    print(f"📦 Total de productos vendidos: {total_productos}")
    print(f"📅 Período consultado: {start.isoformat()} - {end.isoformat()}\n")


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
            report_sales_from_txt(d1, d2)
            input("Presione ENTER para continuar...")

        elif op == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
            input("Presione ENTER para continuar...")

