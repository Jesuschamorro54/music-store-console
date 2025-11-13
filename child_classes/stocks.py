from child_classes.functions.methods import *
from child_classes.functions.path_utils import get_file_path
from child_classes.functions.json_utils import append_to_json_file
import json


class Stock:
    def _init_(self):
        self.container = None
        self._stock_info = {
            "id": None,
            "name": None,
            "lot": None,
            "precio_compra": None,
            "precio_venta": None,
        }

    @property
    def stock(self):
        return self._stock_info

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
                
                # Calcular ganancia si existen los precios
                if self.container[i].get('precio_compra') and self.container[i].get('precio_venta'):
                    ganancia = self.container[i]['precio_venta'] - self.container[i]['precio_compra']
                    porcentaje = (ganancia / self.container[i]['precio_compra']) * 100
                    print(f"|Ganancia/Und   |: ${ganancia:,.2f} ({porcentaje:.1f}%)")
                print(f"{'='*50}\n")
                return 0
        print("❌ No se encuentra el inventario")
    
    def show_catalog(self):
        """Muestra el catálogo completo de productos disponibles"""
        file_path = get_file_path("stocktaking.json")
        self.container = return_exist(file_path)
        
        if not self.container:
            print("❌ No hay productos en el inventario")
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