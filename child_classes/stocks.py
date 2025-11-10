from child_classes.functions.methods import *
from child_classes.functions.path_utilis import get_file_path
from child_classes.functions.json_utilis import append_to_json_file
import json
import os

class Stock:
<<<<<<< HEAD
    def __init__(self):
=======
    def __init__(self, id, name, lot, purchase_price, sale_price):
        self.id = id
        self.name = name
        self.lot = lot
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.file = None
>>>>>>> 6d1c864ee5396e555d1adaaa4cbc922bcb051c07
        self.container = None
        self._stock_info = {
            "id": None,
            "name": None,
            "lot": None,
<<<<<<< HEAD
            "precio_compra": None,
            "precio_venta": None,
=======
            "purchase_price": None,
            "sale_price": None,
>>>>>>> 6d1c864ee5396e555d1adaaa4cbc922bcb051c07
        }
class StockManager:
    def __init__(self):
        self.file_path = os.path.join("files", "stock.json")
        os.makedirs("files", exist_ok=True)
        self.stocks = self.load_stock()

    def load_stock(self):
        if not os.path.exists(self.file_path):
            print("Archivo stock.json no encontrado, se creará uno nuevo.")
            with open(self.file_path, "w") as f:
                json.dump([], f)
            return []
        else:
            with open(self.file_path, "r") as f:
                return json.load(f)

<<<<<<< HEAD
    @stock.setter
    def stock(self, info):
        i = 0
        for key in self._stock_info:
            self._stock_info[key] = info[i]
            i += 1
        append_to_json_file("stocktaking.json", self._stock_info)

    def show_stock(self, ide):
        file_path = get_file_path("stocktaking.json")
        self.container = return_exist(file_path)

        for i in range(len(self.container)):
            if self.container[i]["id"] == ide:
                print(f"\n{'='*50}")
                print(f"  {'INFORMACIÓN DEL PRODUCTO':^46}")
                print(f"{'='*50}")
                print(f"|ID             |: {self.container[i]['id']}")
                print(f"|Nombre         |: {self.container[i]['name']}")
                print(f"|Stock          |: {self.container[i]['lot']} unidades")
                print(f"|Precio Compra  |: ${self.container[i].get('precio_compra', 0):,.2f}")
                print(f"|Precio Venta   |: ${self.container[i].get('precio_venta', 0):,.2f}")
                
                if self.container[i].get('precio_compra') and self.container[i].get('precio_venta'):
                    ganancia = self.container[i]['precio_venta'] - self.container[i]['precio_compra']
                    porcentaje = (ganancia / self.container[i]['precio_compra']) * 100
                    print(f"|Ganancia/Und   |: ${ganancia:,.2f} ({porcentaje:.1f}%)")
                print(f"{'='*50}\n")
                return 0
        print("No se encuentra el inventario")
    
    def show_catalog(self):
        file_path = get_file_path("stocktaking.json")
        self.container = return_exist(file_path)
        
        if not self.container:
            print("No hay productos en el inventario")
            return
        
        print(f"\n{'='*80}")
        print(f"  {'CATÁLOGO DE PRODUCTOS':^76}")
        print(f"{'='*80}")
        print(f"{'ID':<5} {'PRODUCTO':<25} {'STOCK':<10} {'P.VENTA':<15} {'DISPONIBLE':<15}")
        print(f"{'-'*80}")
        
        for producto in self.container:
            stock_status = "✓ Disponible" if producto['lot'] > 0 else "✗ Agotado"
            precio_venta = producto.get('precio_venta', 0)
            
            print(f"{producto['id']:<5} {producto['name']:<25} {producto['lot']:<10} "
                  f"${precio_venta:>12,.2f} {stock_status:<15}")
        
        print(f"{'='*80}\n")
=======
    def save_stock(self):
        with open(self.file_path, "w") as f:
            json.dump(self.stocks, f, indent=4)

    def show_stock(self):
        if not self.stocks:
            print("No hay productos registrados en el inventario.")
            return

        print("\n--- INVENTARIO DE PRODUCTOS ---")
        print("{:<5} {:<20} {:<10} {:<15} {:<15}".format(
            "ID", "Producto", "Stock", "Compra ($)", "Venta ($)"
        ))
        print("-" * 70)

        for product in self.stocks:
            print("{:<5} {:<20} {:<10} {:<15} {:<15}".format(
                product.get("id", ""),
                product.get("name", ""),
                product.get("lot", ""),
                product.get("purchase_price", ""),
                product.get("sale_price", "")
            ))

    def add_product(self, id, name, lot, purchase_price, sale_price):
        new_product = {
            "id": id,
            "name": name,
            "lot": lot,
            "purchase_price": purchase_price,
            "sale_price": sale_price
        }
        self.stocks.append(new_product)
        self.save_stock()
        print(f"✅ Producto '{name}' agregado correctamente al inventario.")
>>>>>>> 6d1c864ee5396e555d1adaaa4cbc922bcb051c07
