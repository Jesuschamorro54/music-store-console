import json
import os

class Facture:

    @staticmethod
    def write_into(path, obj):
    

            # Convertir objetos a diccionario si tienen __dict__
        if hasattr(obj, "__dict__"):
            obj = obj.__dict__

        # Asegurar carpeta
        dirpath = os.path.dirname(path)
        if dirpath and not os.path.exists(dirpath):
            os.makedirs(dirpath, exist_ok=True)

        # Crear archivo si no existe
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4, ensure_ascii=False)

        # Cargar contenido actual
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Si no es lista, forzar a lista
                if not isinstance(data, list):
                    data = []
        except json.JSONDecodeError:
            data = []

    # Agregar la nueva factura
        data.append(obj)

        # 🔥 GUARDAR CORRECTAMENTE 🔥
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    #    Debug opcional
        print("\n=== FACTURA GUARDADA ===")
        print(json.dumps(obj, indent=4, ensure_ascii=False))
        print("========================\n")


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
        print(f"Proveedor ID: {factura.get('supplier_id')}")

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


