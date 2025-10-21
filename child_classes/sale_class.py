from parent_classes.facture_class import Facture
from child_classes.functions.validations import *
from child_classes.functions.path_utils import get_file_path

# clases que dan el funcionamiento de alguanas extructuras


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
        # send products
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