import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from child_classes.functions.json_utils import append_to_json_file, read_json_file, update_json_file

class Facture:
    def _init_(self):
        self.dictionary = None
        self.stock = None

    def write_into(self, path, data):
        filename = os.path.basename(path)
        append_to_json_file(filename, data)
    def read_file(self, path):
        filename = os.path.basename(path)
        return read_json_file(filename)

    def update_stock(self, products, doc):
        dictionary = read_json_file("stocktaking.json")

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
    
        update_json_file("stocktaking.json", dictionary)