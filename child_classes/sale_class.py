import os
from parent_classes.facture_class import Facture
from child_classes.functions.validations import valid_date, return_exist


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
        # actualizar stock
        self.update_stock(info[2], "sale")

        for i, key in enumerate(self._sale_info):
            self._sale_info[key] = info[i]

        file_path = os.path.join("child_classes", "files", "sale.txt")
        self.write_into(file_path, self._sale_info)

    def show_range_date(self, date_init, date_final):
        if not (valid_date(date_init) and valid_date(date_final)):
            return print("El rango de fecha es invalido")

        file_path = os.path.join("child_classes", "files", "sale.txt")
        self.container = return_exist(file_path)

        for item in self.container:
            if date_init <= item["date"] <= date_final:
                print(f"\033[36m\n-- Detalle de la venta --\033[39m")
                print(f"|ID Sale   | -> |{item['id']}|")
                print(f"|ID Client | -> |{item['client']}|")
                print(f"|Products  |")
                for key, val in item["products"].items():
                    print(f"\t\033[31m{key}: {val}\033[39m")
                print(f"|Date      | -> |{item['date']}|")

    def show_by_id(self, ide):
        file_path = os.path.join("child_classes", "files", "sale.txt")
        self.container = return_exist(file_path)

        for item in self.container:
            if item["id"] == ide:
                print(f"\033[36m\n-- Detalle de la venta --\033[39m")
                print(f"|ID Sale   | -> {item['id']}")
                print(f"|ID Client | -> {item['client']}")
                print(f"|Products  |")
                for key, val in item["products"].items():
                    print(f"\t\033[31m{key}: {val}\033[39m")
                print(f"|Date      | -> {item['date']}")
                return
        print("No se encuentra la venta")
