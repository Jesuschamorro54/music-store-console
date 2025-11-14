import os
import json
from datetime import datetime


class Sale:
    def __init__(self):
        self.sales_file = "files/sale.json"
        os.makedirs("files", exist_ok=True)

        if not os.path.exists(self.sales_file):
            with open(self.sales_file, "w") as file:
                json.dump([], file, indent=4)

    def load_sales(self):
        with open(self.sales_file, "r") as file:
            return json.load(file)

    def save_sales(self, sales):
        with open(self.sales_file, "w") as file:
            json.dump(sales, file, indent=4)

    def register_sale(self, stock, client):
        # Mostrar inventario actual
        stock.show_stock()

        product_name = input("Ingrese el nombre del producto que desea comprar: ").strip()
        quantity = int(input("Ingrese la cantidad: "))

        # Validar existencia del producto
        product = stock.find_product(product_name)

        if not product:
            print("❌ El producto no existe.")
            return

        if quantity > product["quantity"]:
            print("❌ Stock insuficiente.")
            return

        # Reducir inventario
        stock.update_stock(product_name, -quantity)

        # Cargar ventas
        sales = self.load_sales()

        # Crear venta
        new_sale = {
            "product": product_name,
            "quantity": quantity,
            "price": product["price"],
            "total": product["price"] * quantity,
            "client": client.get_random_client(),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        sales.append(new_sale)
        self.save_sales(sales)

        print("\n✅ Venta registrada con éxito.")
        print(f"📦 Producto: {product_name}")
        print(f"🧮 Total: {new_sale['total']}")
        print(f"👤 Cliente: {new_sale['client']}")
        print("------------------------------")
