import json
from datetime import datetime

class Buy:

    def __init__(self):
        self.file_path = "files/buys.json"
        self.supplier_file = "files/supplier.json"
        self.stock_file = "files/stocktaking.json"

    # ========================= CARGAR TODAS LAS COMPRAS =========================
    def load_all(self):
        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except:
            return []

   
   
    # ========================= MÉTODO PRINCIPAL PARA REGISTRAR COMPRA =========================
    def make_buy(self):
        print("\n=== REGISTRAR COMPRA ===")

        # ID FACTURA AUTOMÁTICO
        factura_id = len(self.load_all()) + 1

        # ================= VALIDAR PROVEEDOR =================
        while True:
            sup = input("|ID Proveedor     |: ")
            if self.validate_supplier(sup):
                supplier_id = int(sup)
                break
            else:
                print("El proveedor no existe.")

        # ================= REGISTRAR PRODUCTOS =================
        productos = {}

        while True:
            nombre = input("Producto: ")
            cantidad = int(input("Cantidad: "))
            precio = int(input("Precio unidad: "))

            productos[nombre] = {
                "cantidad": cantidad,
                "precio": precio
            }

            seguir = input("¿Agregar otro producto? (s/n): ").lower()
            if seguir != "s":
                break

        # ================= FECHA =================
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return [factura_id, supplier_id, productos, fecha]

    # ========================= GUARDAR COMPRA =========================
    @property
    def buy(self):
        return None

    @buy.setter
    def buy(self, info):
        supplier_id, data = info
        all_buys = self.load_all()

        new_buy = {
            "id": data[0],
            "supplier_id": supplier_id,
            "products": data[1],
            "date": data[2]
        }

        all_buys.append(new_buy)

        with open(self.file_path, "w") as f:
            json.dump(all_buys, f, indent=4)

        print("\n ✔ Compra guardada en buys.json")


    # ========================= ACTUALIZAR STOCK =========================
    def update_stock(self, product, qty):
        try:
            with open(self.stock_file, "r") as f:
                stock = json.load(f)
        except:
            stock = []

        # Buscar producto
        for item in stock:
            if item["product"] == product:
                item["qty"] += qty
                break
        else:
            # Si no existe, lo crea
            stock.append({
                "product": product,
                "qty": qty
            })

        with open(self.stock_file, "w") as f:
            json.dump(stock, f, indent=4)

        print(f"📦 Stock actualizado: +{qty} → {product}")
