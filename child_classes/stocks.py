from child_classes.functions.methods import *
import json
import os

class Stock:
    def _init_(self, id, name, lot, purchase_price, sale_price):
        self.id = id
        self.name = name
        self.lot = lot
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.file = None
        self.container = None
        self._stock_info = {
            "id": None,
            "name": None,
            "lot": None,
            "purchase_price": None,
            "sale_price": None,
        }

    @property
    def stock(self):
        return self._stock_info

    @stock.setter
    def stock(self, info):
        i = 0
        for key in self._stock_info:
            self._stock_info[key] = info[i]
            i += 1
        ("stocktaking.json", self._stock_info)

    def show_stock(self, ide):
        file_path = get_file_path("stocktaking.json")
        self.container = return_exist(file_path)


    def load_stock(self):
        if not os.path.exists(self.file_path):
            print("Archivo stock.json no encontrado, se creará uno nuevo.")
            with open(self.file_path, "w") as f:
                json.dump([], f)
            return []
        else:
            with open(self.file_path, "r") as f:
                return json.load(f)

    def save_stock(self):
        with open(self.file_path, "w") as f:
            json.dump(self.stocks, f, indent=4)

    def show_stock(self):
        if not self.stocks:
            print("No hay productos registrados en el inventario.")
            return

        print("\n--- INVENTARIO DE PRODUCTOS ---")
        print("{:<5} {:<20} {:<10} {:<15} {:<15}".format(
            "ID", "Producto", "Stock", "Compra ($)", "Venta ($)"
        ))
        print("-" * 70)

        for product in self.stocks:
            print("{:<5} {:<20} {:<10} {:<15} {:<15}".format(
                product.get("id", ""),
                product.get("name", ""),
                product.get("lot", ""),
                product.get("purchase_price", ""),
                product.get("sale_price", "")
            ))

    def add_product(self, id, name, lot, purchase_price, sale_price):
        new_product = {
            "id": id,
            "name": name,
            "lot": lot,
            "purchase_price": purchase_price,
            "sale_price": sale_price
        }
        self.stocks.append(new_product)
        self.save_stock()
        print(f"Producto '{name}' agregado correctamente al inventario.")