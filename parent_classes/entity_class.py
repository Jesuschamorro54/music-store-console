import json
import os
import sys

# Añadir el directorio raíz al path para poder importar módulos desde cualquier nivel
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from child_classes.functions.json_utils import append_to_json_file, read_json_file


class Entity:
    def __init__(self):
        self.dictionary = None

    #  Write file
    def write_into(self, path, data):
        # Extraer solo el nombre del archivo de la ruta completa
        filename = os.path.basename(path)
        append_to_json_file(filename, data)

    #  Read file
    def read_file(self, path):
        # Extraer solo el nombre del archivo de la ruta completa
        filename = os.path.basename(path)
        return read_json_file(filename)
    
    # Métodos de validación comunes
    def _validate_id(self):
        """Solicita y valida un ID numérico"""
        while True:
            try:
                ide = int(input("|Identificacion|: "))
                return ide
            except ValueError:
                print("❌ Error: Debe ingresar un número válido")
    
    def _validate_email(self):
        """Solicita y valida un correo electrónico"""
        while True:
            email = input("|Correo        |: ")
            if "@" in email and "." in email.split("@")[1]:
                return email
            print("❌ Error: Correo electrónico inválido")
    
    def _validate_phone(self):
        """Solicita y valida un número de teléfono"""
        while True:
            try:
                phone = input("|Telefono      |: ")
                if len(phone) >= 7:
                    return phone
                print("❌ Error: Teléfono debe tener al menos 7 dígitos")
            except ValueError:
                print("❌ Error: Debe ingresar un número válido")
    
    def capture_data(self):
        """
        Método base para capturar datos de una entidad.
        Este método debe ser sobrescrito por las clases hijas (polimorfismo).
        """
        raise NotImplementedError("Las clases hijas deben implementar capture_data()")
