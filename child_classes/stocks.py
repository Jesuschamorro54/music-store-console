from child_classes.functions.methods import *
import json


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
        i = 0
        for key in self._stock_info:
            self._stock_info[key] = info[i]
            i += 1
        self.file = open(f"C:/Users/ESTUDIANTES/Documents/fundamntos_xd/music-store-console/files/stocktaking.json", "a+", self._client_info)
        text = json.dumps(self._stock_info)
        self.file.write(f"{text}\n")
        self.file.close()

    def show_stock(self, ide):
        self.container = return_exist("C:/Users/ESTUDIANTES/Documents/fundamntos_xd/music-store-console/files/stocktaking.json", self._client_info)

        for i in range(len(self.container)):
            if self.container[i]["id"] == ide:
                print(f"|ID   |: {self.container[i]['id']}")
                print(f"|Name |: {self.container[i]['name']}")
                print(f"|Lot  |: {self.container[i]['lot']}")
                return 0
        print("No se encuentra el inventario")
