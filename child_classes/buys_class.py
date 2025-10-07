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
        # send products for update
        self.update_stock(info[2], "buy")

        i = 0
        for key in self._sale_info:
            self._sale_info[key] = info[i]
            i += 1
        self.write_into("/poo/music-store-console/files/buys.txt", self._sale_info)
