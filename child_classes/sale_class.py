from parent_classes.facture_class import Facture
from child_classes.functions.validations import *
import datetime

class Sale(Facture):
    def __init__(self):
        super().__init__()
        self.container = None
        self._sale_info = {
            "id": None,
            "client": None,
            "products": {},
            "date": None,
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
            return print("El rango de fecha es invalido")

        self.container = return_exist("C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/sale.json")

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
        self.container = return_exist("C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/sale.json")
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

    def parse_date(self, fecha):
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
    
    def report_sales_from_json(self, date1, date2):
        try:
            start = self.parse_date(date1)
            end = self.parse_date(date2)
        except ValueError as e:
            print("Error en fechas:", e)
            return

        if start > end:
            print("La fecha 'Desde' no puede ser mayor que 'Hasta'.")
            return

        ventas = []
        with open("C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/sale.json", "r", encoding="utf-8") as f:
            for ln in f:
                ln = ln.strip()
                if not ln:
                    continue
                try:
                    obj = json.loads(ln)
                except Exception:
                    print("Advertencia: línea de ventas inválida:", ln[:120])
                    continue

                date_str = obj.get("date") or obj.get("fecha")
                try:
                    date_obj = self.parse_date(date_str)
                except Exception:
                    print("Advertencia: fecha inválida en línea:", ln[:120])
                    continue

                ventas.append({
                    "id": obj.get("id"),
                    "client": obj.get("client") or obj.get("cliente"),
                    "date": date_obj,
                    "products": obj.get("products") or obj.get("productos") or {},
                })

        ventas_filtradas = [v for v in ventas if start <= v["date"] <= end]

        print(f"\nREPORTE DE VENTAS DESDE {start.isoformat()} HASTA {end.isoformat()}")
        print("════════════════════════════════════════════════════════════\n")
        if not ventas_filtradas:
            print("No se encontraron ventas en el rango indicado.\n")
            return

        total_productos = 0
        for i, venta in enumerate(ventas_filtradas, start=1):
            print(f"Venta #{i}")
            print(f"  ├── ID Venta: {venta.get('id')}")
            print(f"  ├── Cliente: {venta.get('client')}")
            print(f"  ├── Fecha: {venta.get('date').isoformat()}")
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
        print(f"Total de ventas en el período: {len(ventas_filtradas)}")
        print(f"Total de productos vendidos: {total_productos}")
        print(f"Período consultado: {start.isoformat()} - {end.isoformat()}\n")
