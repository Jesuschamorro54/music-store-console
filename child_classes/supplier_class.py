import os
from parent_classes.entity_class import Entity


class Supplier(Entity):
    def __init__(self):
        super().__init__()
        self._supplier_info = {
            "id": None,
            "name": None,
            "email": None,
            "cellphone": None,
        }

    @property
    def supplier(self):
        return self._supplier_info

    @supplier.setter
    def supplier(self, info):
        for i, key in enumerate(self._supplier_info):
            self._supplier_info[key] = info[i]

        file_path = os.path.join("child_classes", "files", "supplier.txt")
        self.write_into(file_path, self._supplier_info)
