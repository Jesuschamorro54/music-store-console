import os
from parent_classes.entity_class import Entity
from child_classes.functions.methods import *
from child_classes.functions.path_utils import get_file_path

class Client(Entity):
    def __init__(self):
        super().__init__()
        self.container = None
        self._client_info = {
            "id": None,
            "name": None,
            "last_name": None,
            "email": None,
            "cellphone": None}

    @property
    def client(self):
        return self._client_info

    @client.setter
    def client(self, info):
        i = 0
        for key in self._client_info:
            self._client_info[key] = info[i]
            i += 1

        file_path = get_file_path("client.json")
        self.write_into(file_path, self._client_info)

    def capture_data(self):
        print("\n=== REGISTRO DE CLIENTE ===")
        
        ide = self._validate_id()
        
        name = input("|Nombre        |: ").strip()
        while not name:
            print(" Error: El nombre no puede estar vacío")
            name = input("|Nombre        |: ").strip()
        
        last_name = input("|Apellido      |: ").strip()
        while not last_name:
            print(" Error: El apellido no puede estar vacío")
            last_name = input("|Apellido      |: ").strip()
        
        email = self._validate_email()
        phone = self._validate_phone()
        
        return [ide, name, last_name, email, phone]

    def show_client(self, ide):
        file_path = get_file_path("client.json")
        self.container = return_exist(file_path)

        for i in range(len(self.container)):
            name_complet = self.container[i]["name"] + " " + self.container[i]["last_name"]
            if self.container[i]["id"] == ide:
                print(f"|ID              |: {self.container[i]['id']}")
                print(f"|Name            |: {name_complet}")
                print(f"|Email           |: {self.container[i]['email']}")
                print(f"|Cellphhone      |: {self.container[i]['cellphone']}")
                return 0
        print("No se encuentra el cliente")