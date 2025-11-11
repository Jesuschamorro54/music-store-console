import os
from parent_classes.facture_class import Facture

class Buy(Facture):
    def __init__(self):
        super().__init__()
        self._sale_info = {
            "ID": None,
            "Supplier": None,
            "Products": {},
            "Date": None,
            }

    @property
    def buy(self):
        return self._sale_info

    @buy.setter
    def buy(self, info):
      
        self.update_stock(info[2], "buy")

        i = 0
        for key in self._sale_info:
            self._sale_info[key] = info[i]
            i += 1
        base_path = os.path.dirname(os.path.abspath(__file__))  
        file_path = os.path.join(base_path, "..", "files", "buys.json")  
        file_path = os.path.normpath(file_path)  
        self.write_into(file_path, self._sale_info)
