from parent_classes.entity_class import Entity
from child_classes.functions.path_utils import get_file_path


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
        file_path = get_file_path("supplier.json")
        self.write_into(file_path, self._supplier_info)
    
    def capture_data(self):
        """
        Implementación polimórfica para capturar datos de un proveedor.
        Sobrescribe el método de la clase padre Entity.
        A diferencia de Client, Supplier solo captura nombre (no apellido).
        """
        print("\n=== REGISTRO DE PROVEEDOR ===")
        
        # Capturar ID usando validación de la clase padre
        ide = self._validate_id()
        
        # Capturar solo nombre (específico de Proveedor - sin apellido)
        name = input("|Nombre        |: ").strip()
        while not name:
            print("❌ Error: El nombre no puede estar vacío")
            name = input("|Nombre        |: ").strip()
        
        # Capturar email y teléfono usando validación de la clase padre
        email = self._validate_email()
        phone = self._validate_phone()
        
        # Retornar datos en el orden esperado (sin apellido)
        return [ide, name, email, phone]
