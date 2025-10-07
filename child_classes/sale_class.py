import datetime
import os
from child_classes.functions.validations import *
# clases que dan el funcionamiento de alguanas extructuras


class Sale():
    def __init__(self):
        super().__init__()
        self.container = None

        self._sale_info = {
            "id": None,
            "client": None,
            "products": {},
            "date": None,
            }
        
        self.sales = []
        self.file_path = "C:/desarrollo/music-store-console/files/sale.txt"

        # cargar archivo si existe
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding="utf-8") as f:
                try:

                    # HAY UN ERROR AL LEER LOS DATOS DEL ARCHIVO

                    data = json.load(f)
                    # convertir fechas a datetime
                    for venta in data:
                        venta["fecha"] = self.parse_date(venta["fecha"])
                    self.sales = data
                except json.JSONDecodeError as e:
                    print("Error al leer el archivo", e)
                    self.sales = []

    @property
    def sale(self):
        return self._sale_info

    @sale.setter
    def sale(self, info):
        # send products
        self.update_stock(info[2], "sale")
        i = 0
        for key in self._sale_info:
            self._sale_info[key] = info[i]
            i += 1
        self.write_into("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/sale.txt", self._sale_info)

    def show_range_date(self, date_init, date_final):
        if not valid_date(date_init) and not valid_date(date_final):
            return print("El rango de fecha es invalido")

        self.container = return_exist("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/sale.txt")

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
        self.container = return_exist("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/sale.txt")
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

    def show_report(self, date1, date2):
        try:
            start = self.parse_date(date1)
            end = self.parse_date(date2)
        except ValueError as e:
            print("Error en fechas:", e)
            return

        if start > end:
            print("La fecha 'Desde' no puede ser mayor que 'Hasta'.")
            return

        print(f"\n📊 REPORTE DE VENTAS SOLICITADAS DEL {start.isoformat()} AL {end.isoformat()}")
        print("════════════════════════════════════════════════════════════")

        print("ventas encontradas", self.sales)

        ventas_filtradas = [
            venta for venta in self.sales
            if start <= self.parse_date(venta["fecha"]) <= end
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
