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
        for i in range(len(self.container)):
            if self.container[i]["id"] == ide:
                print(f"|ID            |: {self.container[i]['id']}")
                print(f"|Name            |: {self.container[i]['name']} {self.container[i]['last_name']}")
                print(f"|Email           |: {self.container[i]['email']}")
                print(f"|Cellphhone      |: {self.container[i]['cellphone']}")
                return 0
        print("No se encuentra el cliente")

    def return_exist(path):
        data_list = []
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:  # si no está vacía
                    try:
                        data_list.append(json.loads(line))
                    except json.JSONDecodeError:
                        print(f"Error al decodificar línea: {line}")
        return data_list

        
