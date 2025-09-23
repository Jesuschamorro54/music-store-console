from parent_classes.entity_class import Entity


class Supplier(Entity):
    def __init__(self):
        super().__init__()
        self._supplier_info = {
            "id": None,
            "name": None,
            "email": None,
            "cellphone": None}

    @property
    def supplier(self):
        return self._supplier_info

    @supplier.setter
    def supplier(self, info):
        i = 0
        for key in self._supplier_info:
            self._supplier_info[key] = info[i]
            i += 1
        self.write_into("/Users/NEIDER/tienda m/music-store-console/files/supplier.txt", self._supplier_info)
