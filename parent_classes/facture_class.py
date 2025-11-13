import json
import os

class Facture:
    def __init__(self):
        # Construye rutas dinámicamente (sin rutas absolutas)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        self.files_dir = os.path.join(base_dir, "files")
        self.stock_path = os.path.join(self.files_dir, "stock.json")

        self.file = None
        self.container = []
        self.temp = []

    def update_stock(self, products, type_):
        """
        Actualiza el stock según el tipo de operación:
        - type_ == "sale": resta del inventario
        - type_ == "buy":  suma al inventario
        """
        if not os.path.exists(self.stock_path):
            print("⚠️ No se encontró el archivo de stock.")
            return

        with open(self.stock_path, "r", encoding="utf-8") as f:
            try:
                self.container = json.load(f)
            except json.JSONDecodeError:
                print("⚠️ El archivo de stock está vacío o dañado.")
                return

        for name, amount in products.items():
            for item in self.container:
                # Admite claves "name" o "nombre"
                item_name = item.get("name") or item.get("nombre")

                if item_name and item_name.lower() == name.lower():
                    # Admite "quantity" o "lot" como cantidad
                    stock_quantity = item.get("quantity") or item.get("lot") or 0

                    if type_ == "sale":
                        if stock_quantity >= amount:
                            stock_quantity -= amount
                        else:
                            print(f"⚠️ No hay suficiente stock para '{name}'.")
                            continue
                    elif type_ == "buy":
                        stock_quantity += amount

                    # Actualiza el valor correcto
                    if "quantity" in item:
                        item["quantity"] = stock_quantity
                    else:
                        item["lot"] = stock_quantity
                    break

        # Guarda los cambios
        with open(self.stock_path, "w", encoding="utf-8") as f:
            json.dump(self.container, f, indent=4)

    def write_into(self, path, data):
        """Agrega un nuevo registro JSON en el archivo dado."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        all_data = []

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                try:
                    all_data = json.load(f)
                except json.JSONDecodeError:
                    all_data = []

        all_data.append(data)

        with open(path, "w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4)
