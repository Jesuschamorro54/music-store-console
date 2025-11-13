from parent_classes.entity_class import Entity
from child_classes.path_manager import get_file_path # funcion para la ruta dinamica

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
        self.write_into(get_file_path("supplier.json"), self._supplier_info) # dinamica
