import json
import os
import sys

# Añadir el directorio raíz al path para poder importar módulos desde cualquier nivel
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(_file_))))

from child_classes.functions.json_utils import append_to_json_file, read_json_file, update_json_file


class Facture:
    def _init_(self):
        self.dictionary = None
        self.stock = None

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

    def update_stock(self, products, doc):
        # Leer inventario actual
        dictionary = read_json_file("stocktaking.json")

        # Check if it is a purchase or a sale 
        if doc == "sale":
            for key in products:
                for i in range(len(dictionary)):
                    if dictionary[i]["name"].lower() in key.lower():
                        dictionary[i]["lot"] -= products[key]
        else:
            for key in products:
                for i in range(len(dictionary)):
                    if dictionary[i]["name"].lower() in key.lower():
                        dictionary[i]["lot"] += products[key]
        
        # Actualizar archivo con los nuevos valores
        update_json_file("stocktaking.json", dictionary)