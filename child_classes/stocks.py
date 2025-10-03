import os
import json
from child_classes.functions.validations import return_exist


class Stock:
    def __init__(self):
        self.file = None
        self.container = None
        self._stock_info = {
            "id": None,
            "name": None,
            "lot": None,
        }

    @property
    def stock(self):
        return self._stock_info

    @stock.setter
    def stock(self, info):
        for i, key in enumerate(self._stock_info):
            self._stock_info[key] = info[i]

        file_path = os.path.join("child_classes", "files", "stocktaking.txt")
        with open(file_path, "a+", encoding="utf-8") as f:
            text = json.dumps(self._stock_info, ensure_ascii=False)
            f.write(f"{text}\n")

    def show_stock(self, ide):
        file_path = os.path.join("child_classes", "files", "stocktaking.txt")
        self.container = return_exist(file_path)

        for item in self.container:
            if item["id"] == ide:
                print(f"|ID   |: {item['id']}")
                print(f"|Name |: {item['name']}")
                print(f"|Lot  |: {item['lot']}")
                return
        print("No se encuentra el inventario")

