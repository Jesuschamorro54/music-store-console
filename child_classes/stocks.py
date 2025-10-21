from child_classes.functions.methods import *
from child_classes.functions.path_utils import get_file_path
from child_classes.functions.json_utils import append_to_json_file
import json


class Stock:
    def __init__(self):
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
        i = 0
        for key in self._stock_info:
            self._stock_info[key] = info[i]
            i += 1
        append_to_json_file("stocktaking.json", self._stock_info)

    def show_stock(self, ide):
        file_path = get_file_path("stocktaking.json")
        self.container = return_exist(file_path)

        for i in range(len(self.container)):
            if self.container[i]["id"] == ide:
                print(f"|ID   |: {self.container[i]['id']}")
                print(f"|Name |: {self.container[i]['name']}")
                print(f"|Lot  |: {self.container[i]['lot']}")
                return 0
        print("No se encuentra el inventario")
