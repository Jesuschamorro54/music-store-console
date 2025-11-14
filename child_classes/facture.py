import json
import os

class Facture:
    @staticmethod
    def write_into(path, obj):

        # Asegurar formato dict
        if hasattr(obj, "__dict__"):
            obj = obj.__dict__

        if isinstance(obj, list):
            obj = [x.__dict__ if hasattr(x, "__dict__") else x for x in obj]

        # Crear carpeta si no existe
        dirpath = os.path.dirname(path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)

        # Crear archivo si no existe
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

        # Cargar contenido actual
        with open(path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

        if isinstance(data, dict):
            data = [data]

        # Añadir factura nueva
        data.append(obj)

        # Guardar
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    # =========================================================
    def load_last(self):
        path = "files/factura.json"

        if not os.path.exists(path):
            return None

        try:
            with open(path, "r", encoding="utf-8") as f:
                facturas = json.load(f)
                if isinstance(facturas, list) and len(facturas) > 0:
                    return facturas[-1]
                else:
                    return None
        except:
            return None

    # =========================================================
    def show(self, factura):
        if not factura:
            print("\nNo hay factura para mostrar.\n")
            return

        print("\n=========== FACTURA RECIENTE ===========")
        print(f"Factura ID: {factura.get('factura_id', 'N/A')}")
        print(f"Proveedor ID: {factura.get('supplier_id', 'N/A')}")
        print(f"Proveedor Nombre: {factura.get('supplier_name', 'N/A')}")
        if factura.get("fecha"):
            print(f"Fecha: {factura.get('fecha')}")
        print("\nProductos:")

        total = 0
        for prod in factura.get("products", []):
            name = prod["name"]
            qty = prod["quantity"]
            price = prod["price"]
            subtotal = prod["subtotal"]
            print(f"- {name}: {qty} x {price} = {subtotal}")
            total += subtotal

        print(f"\nTOTAL: {total}")
        print("==========================================\n")

    # =========================================================
    def update_stock(self, products_dict, mode="buy"):
        try:
            from child_classes.stocks import Stock
            stock_ins = Stock()

            cantidades = {name: info.get("cantidad", 0) for name, info in products_dict.items()}

            if hasattr(stock_ins, "update_stock"):
                stock_ins.update_stock(cantidades, mode)
            elif hasattr(stock_ins, "modify_stock"):
                stock_ins.modify_stock(cantidades, mode)

        except Exception as e:
            print("Error actualizando stock:", e)
