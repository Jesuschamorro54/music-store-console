import os
from parent_classes.entity_class import Entity
from child_classes.functions.methods import *


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

        # Construir la ruta relativa al proyecto
        # base_dir = os.path.dirname(os.path.abspath(__file__))  # carpeta donde está este archivo .py
        # file_path = os.path.join(base_dir, "files", "client.txt")

        # self.write_into(file_path, self._client_info)
        self.write_into("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/client.txt", self._client_info)

    def show_client(self, ide, name):
        self.container = return_exist("/Users/jesuschamorro/Downloads/dev/POO/Parcial_III/child_classes/files/client.txt")

        for i in range(len(self.container)):
            name_complet = self.container[i]["name"] + " " + self.container[i]["last_name"]
            if self.container[i]["id"] == ide and name.lower() in name_complet.lower():
                print(f"|ID              |: {self.container[i]['id']}")
                print(f"|Name            |: {name_complet}")
                print(f"|Email           |: {self.container[i]['email']}")
                print(f"|Cellphhone      |: {self.container[i]['cellphone']}")
                return 0
        print("No se encuentra el cliente")
