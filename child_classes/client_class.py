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
        self.write_into(get_file_path("client.json"), self._client_info) # funcion para la ruta dinamica

    def show_client(self, ide, name): # Demostracion y diseño de la impresion para motrar los datos del usario
        # Cargar clientes
        self.container = return_exist(get_file_path("client.json"))

        # Cargar ventas
        sales = return_exist(get_file_path("sale.json"))

        # Cargar stocktaking (precios)
        stock = return_exist(get_file_path("stocktaking.json"))

        # Buscar cliente
        for c in self.container:
            full_name = f"{c['name']} {c['last_name']}"
            if c["id"] == ide and name.lower() in full_name.lower():

                # ---------------- IMPRESIÓN BÁSICA ----------------
                # Aqui se mostraran la informacion basica del usario, de acuerdo al nombre y al ID

                print(f"\n|Ingreso ID:   \033[96m{c['id']}\033[0m\n")

                print(f"\n|ID              |: \033[96m{c['id']}\033[0m")
                print(f"|Name            |: \033[92m{full_name}\033[0m")
                print(f"|Email           |: {c['email']}")
                print(f"|Cellphhone      |: \033[96m{c['cellphone']}\033[0m\n")

                # ---------------- CONTAR COMPRAS ----------------
                # comienza a contar las compras, de acuerdo al ID, del cliente, y asi dar un total de compras
                # recorre todas las compras donde tenga ese ID, y comienza a contarlas para dar un numero de compra en total

                compras_cliente = [s for s in sales if s.get("client") == ide]
                total_compras = len(compras_cliente)
                print(f"Total de veces compradas en la tienda: \033[92m{total_compras}\033[0m")

                # ---------------- CONTAR PRODUCTOS ----------------
                # Comienza a hacer un listado, donde adquiere la Lista de los "Items" o "Productos del usario"

                productos_total = {}
                total_items = 0

                # Recorre cada venta del cliente, Suma en cuantas veces compro en cada producto
                # y por ultimo, Suma el total de Items o Productos comprados

                for venta in compras_cliente:
                    for nombre_producto, cantidad in venta["products"].items():
                        productos_total[nombre_producto] = productos_total.get(nombre_producto, 0) + cantidad
                        total_items += cantidad

                        # Imprime de una forma visual

                print("Productos comprados")
                print(f"    ├── TOTAL: \033[94m{total_items}\033[0m")
                print("    │")

                # ---------------- ÁRBOL DE PRODUCTOS ----------------
                #  Añade un print con estilo, (aplicacion de diseño)

                for i, (prod, cant) in enumerate(productos_total.items()):
                    prefix = "└──" if i == len(productos_total)-1 else "├──"
                    print(f"    {prefix} {prod.capitalize()}: {cant}")

                # ---------------- CALCULAR TOTAL $ ----------------
                # Recorre cada item, o producto comprado por el cliente, despues de eso recorre los precios reales del
                # Archivo Json "Stocktaking.json"
                # Toma su precio, y hace una operacion sencilla, donde multiplica "Precion x Cantidad" para al final sumar Todo

                total_dinero = 0 # Variable por definicion

                for prod, cantidad in productos_total.items():
                    for item in stock:
                        if item["name"].lower() == prod.lower():
                            total_dinero += item["price"] * cantidad

                print(f"\n💰 Total recaudado: \033[96m ${total_dinero:,}\033[0m\n".replace(",", ".")) # Diseño para dar separaciones de valores grandes

                return

        print("No se encuentra el cliente")

