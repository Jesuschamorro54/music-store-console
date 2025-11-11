import os
from parent_classes.entity_class import Entity
from child_classes.functions.methods import *


class Client(Entity):
    def __init__(self):
        super().__init__()
        self.container = None
        self._client_info = {
            "ID": None,
            "Nombre": None,
            "Email": None,
            "Telefono": None
        }

        base_dir = os.path.dirname(os.path.abspath(__file__)) 
        self.file_path = os.path.join(base_dir, "..", "files", "client.json")  
        self.file_path = os.path.normpath(self.file_path)  

    @property
    def client(self):
        return self._client_info

    @client.setter
    def client(self, info):
        i = 0
        for key in self._client_info:
            self._client_info[key] = info[i]
            i += 1

        self.write_into(self.file_path, self._client_info)

    def show_client(self, ide=None, name=None):
        self.container = return_exist(self.file_path)

        for client in self.container:
            full_name = f"{client['name']} {client['last_name']}"
            if (ide is None or client["id"] == ide) and (name is None or name.lower() in full_name.lower()):
                print(f"|ID          |: {client['id']}")
                print(f"|Nombre      |: {full_name}")
                print(f"|Email       |: {client['email']}")
                print(f"|Celular     |: {client['cellphone']}")
                return

        print("No se encuentra el cliente")
