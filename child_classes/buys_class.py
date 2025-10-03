import os
from parent_classes.facture_class import Facture


class Buy(Facture):
    def __init__(self):
        super().__init__()
        self._sale_info = {
            "id": None,
            "supplier": None,
            "products": {},
            "date": None,
        }

    @property
    def buy(self):
        return self._sale_info

    @buy.setter
    def buy(self, info):
        # actualizar inventario
        self.update_stock(info[2], "buy")

        for i, key in enumerate(self._sale_info):
            self._sale_info[key] = info[i]

        file_path = os.path.join("child_classes", "files", "buys.txt")
        self.write_into(file_path, self._sale_info)
