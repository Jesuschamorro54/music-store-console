import os
from parent_classes.entity_class import Entity
from child_classes.functions.methods import *
from child_classes.path_manager import get_file_path # importancio de funcion para la ruta dinamica

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
        
        for i, key in enumerate(self._client_info):
            self._client_info[key] = info[i]
            

        # Construir la ruta relativa al proyecto
        # base_dir = os.path.dirname(os.path.abspath(__file__))  # carpeta donde está este archivo .py
        # file_path = os.path.join(base_dir, "files", "client.json")

        # self.write_into(file_path, self._client_info)
        self.write_into("C:/Users/ESTUDIANTE/Documents/music/music-store-console/files/files/client.json")
    def show_client(self, ide, name):
        self.container = return_exist("C:/Users/ESTUDIANTE/Documents/music/music-store-console/files/files/client.json")

        for i in range(len(self.container)):
            name_complet = self.container[i]["name"] + " " + self.container[i]["last_name"]
            if self.container[i]["id"] == ide and name.lower() in name_complet.lower():
                print(f"|ID              |: {self.container[i]['id']}")
                print(f"|Name            |: {name_complet}")
                print(f"|Email           |: {self.container[i]['email']}")
                print(f"|Cellphhone      |: {self.container[i]['cellphone']}")
                return 0
        print("No se encuentra el cliente")
