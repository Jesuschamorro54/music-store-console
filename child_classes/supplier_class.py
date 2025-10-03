from parent_classes.entity_class import Entity
BASE_DATOS = "/Users/ESTUDIANTES/Documents/Proyecto/music-store-console/files"

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
        self.write_into(F"{BASE_DATOS}/supplier.txt", self._supplier_info)
