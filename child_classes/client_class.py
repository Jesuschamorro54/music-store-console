import os
from parent_classes.entity_class import Entity
from child_classes.functions.methods import *
import json


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

        self.write_into("C:/Users/LAPTOP/Desktop/proyecto semestre 2/music-store-console/files/client.json", self._client_info)

    def show_client(self, ide,):
        file_path = get_file_path("client.json")
        self.container = return_exist(file_path)

        for i in range(len(self.container)):
            name_complet = self.container[i]["name"] 
            if self.container[i]["id"] == ide:
                print(f"|ID              |: {self.container[i]['id']}")
                print(f"|Name            |: {name_complet}")
                print(f"|Email           |: {self.container[i]['email']}")
                print(f"|Cellphhone      |: {self.container[i]['cellphone']}")
                return 0
        print("No se encuentra el cliente")
