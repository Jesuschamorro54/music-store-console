import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from child_classes.functions.json_utils import append_to_json_file, read_json_file

class Entity:
    def _init_(self):
        self.dictionary = None

    def write_into(self, path, data):
        filename = os.path.basename(path)
        append_to_json_file(filename, data)

    def read_file(self, path):
        filename = os.path.basename(path)
        return read_json_file(filename)
    
    def _validate_id(self):
        while True:
            try:
                ide = int(input("|Identificacion|: "))
                return ide
            except ValueError:
                print("Error: Debe ingresar un número válido")
    
    def _validate_email(self):
        while True:
            email = input("|Correo        |: ")
            if "@" in email and "." in email.split("@")[1]:
                return email
            print("Error: Correo electrónico inválido")
    
    def _validate_phone(self):
        while True:
            try:
                phone = input("|Telefono      |: ")
                if len(phone) >= 7:
                    return phone
                print("Error: Teléfono debe tener al menos 7 dígitos")
            except ValueError:
                print("Error: Debe ingresar un número válido")
    
    def capture_data(self):
        raise NotImplementedError("Las clases hijas deben implementar capture_data()")