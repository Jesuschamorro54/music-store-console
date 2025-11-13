from child_classes.functions.validations import *
from child_classes.functions.path_utils import get_file_path
from datetime import datetime
from child_classes.functions.json_utils import read_json_file
from child_classes.stocks import Stock


def get_product_by_id(product_id):
    from child_classes.functions.json_utils import read_json_file
    products = read_json_file("stocktaking.json")
    
    for product in products:
        if product['id'] == product_id:
            return product
    return None


def get_client_by_id(client_id):
    from child_classes.functions.json_utils import read_json_file
    clients = read_json_file("client.json")
    
    for client in clients:
        if client['id'] == client_id:
            return client
    return None


def get_supplier_by_id(supplier_id):
    from child_classes.functions.json_utils import read_json_file
    suppliers = read_json_file("supplier.json")
    
    for supplier in suppliers:
        if supplier['id'] == supplier_id:
            return supplier
    return None


def get_products_by_supplier(supplier_id):
    from child_classes.functions.json_utils import read_json_file
    products = read_json_file("stocktaking.json")
    
    supplier_products = []
    for product in products:
        if product.get('supplier_id') == supplier_id:
            supplier_products.append(product)
    
    return supplier_products


def show_supplier_catalog(supplier_id, supplier_name):
    products = get_products_by_supplier(supplier_id)
    
    if not products:
        print(f"\n El proveedor {supplier_name} no tiene productos registrados")
        return False
    
    print(f"\n{'='*80}")
    print(f"  {'CATÁLOGO DE PRODUCTOS - ' + supplier_name.upper():^76}")
    print(f"{'='*80}")
    print(f"{'ID':<5} {'PRODUCTO':<30} {'STOCK':<10} {'P.COMPRA':<15}")
    print(f"{'-'*80}")
    
    for producto in products:
        precio_compra = producto.get('precio_compra', 0)
        print(f"{producto['id']:<5} {producto['name']:<30} {producto['lot']:<10} "
              f"${precio_compra:>12,.0f}")
    
    print(f"{'='*80}\n")
    return True


def show_cart(carrito, total_venta):
    print(f"\n{'='*70}")
    print(f"  {'CARRITO DE COMPRAS':^66}")
    print(f"{'='*70}")
    if not carrito:
        print("  El carrito está vacío")
    else:
        print(f"{'CANT':>6}  {'PRODUCTO':<30} {'P.UNIT':>12} {'SUBTOTAL':>14}")
        print(f"{'-'*70}")
        for item in carrito:
            print(f"{item['cantidad']:>6}x  {item['nombre']:<30} "
                  f"${item['precio_unitario']:>10,.0f} ${item['subtotal']:>12,.0f}")
        print(f"{'='*70}")
        print(f"{'TOTAL A PAGAR':>52} ${total_venta:>14,.0f}")
        print(f"{'='*70}\n")


def make_sale_buy(entity):
    sale_file_path = get_file_path("sale.json")
    buys_file_path = get_file_path("buys.json")
    ide = define_id(sale_file_path) if entity == "client" else define_id(buys_file_path)
    product = {}
    capsule = []
    entity_id = None

    if entity == "client":
        print("\n==BUSCAR CLIENTE==")
        while True:
            try:
                client_id = int(input("|ID Cliente        |: "))
                client = get_client_by_id(client_id)
                if client:
                    entity_id = client_id
                    print(f"Cliente encontrado: {client['name']} {client['last_name']}")
                    break
                else:
                    print("Cliente no encontrado. Intente nuevamente.")
            except ValueError:
                print(" Debe ingresar un ID numérico válido")
    else:
        print("\n==BUSCAR PROVEEDOR==")
        while True:
            try:
                supplier_id = int(input("|ID Proveedor      |: "))
                supplier = get_supplier_by_id(supplier_id)
                if supplier:
                    entity_id = supplier_id
                    print(f"✓ Proveedor encontrado: {supplier['name']}")
                    break
                else:
                    print(" Proveedor no encontrado. Intente nuevamente.")
            except ValueError:
                print("Debe ingresar un ID numérico válido")

    if entity == "client":
        stock_ins = Stock()
        stock_ins.show_catalog()
    else:
        if not show_supplier_catalog(entity_id, supplier['name']):
            return None  
    
    total_venta = 0
    carrito = []
    agregando_productos = True
    
    while agregando_productos:
        print("\n==AGREGAR PRODUCTOS==")
        
        while True:
            try:
                producto_id = int(input("|ID Producto       |: "))
                if producto_id == 0:
                    if not carrito:
                        print("Debe agregar al menos un producto")
                        continue
                    agregando_productos = False
                    break
                
                producto = get_product_by_id(producto_id)
                if not producto:
                    print("Producto no encontrado")
                    continue
                
                if entity != "client":
                    if producto.get('supplier_id') != entity_id:
                        print("Este producto no pertenece a este proveedor")
                        continue
                
                print(f"✓ Producto: {producto['name']}")
                if entity == "client":
                    print(f"  Precio: ${producto.get('precio_venta', 0):,.0f}")
                    print(f"  Stock disponible: {producto['lot']} unidades")
                else:
                    print(f"  Precio de compra: ${producto.get('precio_compra', 0):,.0f}")
                    print(f"  Stock actual: {producto['lot']} unidades")
                
                while True:
                    try:
                        cantidad = int(input("|Cantidad          |: "))
                        if cantidad <= 0:
                            print("La cantidad debe ser mayor a 0")
                            continue
                        
                        if entity == "client":
                            if cantidad > producto['lot']:
                                print(f"Stock insuficiente. Disponible: {producto['lot']}")
                                continue
                        
                        break
                    except ValueError:
                        print("Debe ingresar un número válido")
                
                precio = producto.get('precio_venta', 0) if entity == "client" else producto.get('precio_compra', 0)
                subtotal = precio * cantidad
                
                product[producto['name']] = cantidad
                carrito.append({
                    'id': producto['id'],
                    'nombre': producto['name'],
                    'cantidad': cantidad,
                    'precio_unitario': precio,
                    'subtotal': subtotal
                })
                
                total_venta += subtotal
                print(f"\n✓ Agregado: {cantidad}x {producto['name']} = ${subtotal:,.0f}")
                
                if entity == "client":
                    while True:
                        print(f"\n{'─'*50}")
                        print("  [1] Agregar más productos")
                        print("  [2] Ver carrito")
                        print("  [3] Ir a pagar")
                        print(f"{'─'*50}")
                        
                        try:
                            opcion = int(input("Seleccione una opción: "))
                            
                            if opcion == 1:
                                break
                            elif opcion == 2:
                                show_cart(carrito, total_venta)
                            elif opcion == 3:
                                agregando_productos = False
                                break
                            else:
                                print("Opción inválida")
                        except ValueError:
                            print(" Debe ingresar un número válido")
                    
                    if not agregando_productos:
                        break
                else:
                    while True:
                        print(f"\n{'─'*50}")
                        print("  [1] Agregar más productos")
                        print("  [2] Ver pedido")
                        print("  [3] Finalizar compra")
                        print(f"{'─'*50}")
                        
                        try:
                            opcion = int(input("Seleccione una opción: "))
                            
                            if opcion == 1:
                                break
                            elif opcion == 2:
                                show_cart(carrito, total_venta)
                            elif opcion == 3:
                                agregando_productos = False
                                break
                            else:
                                print("Opción inválida")
                        except ValueError:
                            print("Debe ingresar un número válido")
                    
                    if not agregando_productos:
                        break
                
            except ValueError:
                print("Debe ingresar un ID numérico válido")

    if entity == "client":
        print(f"\n{'='*70}")
        print(f"  {'RESUMEN FINAL DE LA VENTA':^66}")
        print(f"{'='*70}")
        print(f"  Cliente: {client['name']} {client['last_name']} (ID: {client_id})")
    
        fecha_actual = datetime.now()
        date = fecha_actual.strftime("%Y-%m-%d")
        hora = fecha_actual.strftime("%H:%M:%S")
        
        print(f"  Fecha: {date}")
        print(f"  Hora: {hora}")
        print(f"{'─'*70}")
        
        print(f"{'CANT':>6}  {'PRODUCTO':<30} {'P.UNIT':>12} {'SUBTOTAL':>14}")
        print(f"{'-'*70}")
        for item in carrito:
            print(f"{item['cantidad']:>6}x  {item['nombre']:<30} "
                  f"${item['precio_unitario']:>10,.0f} ${item['subtotal']:>12,.0f}")
        
        print(f"{'='*70}")
        print(f"{'TOTAL A PAGAR':>52} ${total_venta:>14,.0f}")
        print(f"{'='*70}")
        
        print("\n¿Confirmar la venta?")
        confirmar = input("[S] Sí - Procesar pago  [N] No - Cancelar: ").lower()
        
        if confirmar != 's':
            print("\nVenta cancelada")
            return None
        
        print("\nVenta procesada exitosamente!")
        print(f"Factura #: {ide}")
        print(f"Total: ${total_venta:,.0f}")
    else:
        print(f"\n{'='*70}")
        print(f"  {'FACTURA DE COMPRA':^66}")
        print(f"{'='*70}")
        print(f"  Proveedor: {supplier['name']} (ID: {supplier_id})")
        
        fecha_actual = datetime.now()
        date = fecha_actual.strftime("%Y-%m-%d")
        hora = fecha_actual.strftime("%H:%M:%S")
        
        print(f"  Fecha: {date}")
        print(f"  Hora: {hora}")
        print(f"{'─'*70}")
        
        print(f"{'CANT':>6}  {'PRODUCTO':<30} {'P.UNIT':>12} {'SUBTOTAL':>14}")
        print(f"{'-'*70}")
        for item in carrito:
            print(f"{item['cantidad']:>6}x  {item['nombre']:<30} "
                  f"${item['precio_unitario']:>10,.0f} ${item['subtotal']:>12,.0f}")
        
        print(f"{'='*70}")
        print(f"{'TOTAL DE LA COMPRA':>52} ${total_venta:>14,.0f}")
        print(f"{'='*70}")
        
        print("\n¿Confirmar la compra?")
        confirmar = input("[S] Sí - Registrar compra  [N] No - Cancelar: ").lower()
        
        if confirmar != 's':
            print("\n Compra cancelada")
            return None
        
        print("\nCompra registrada exitosamente!")
        print(f"Orden de Compra #: {ide}")
        print(f"Total: ${total_venta:,.0f}")
        print(f"Inventario actualizado")

    capsule.append(ide)         
    capsule.append(entity_id)  
    capsule.append(product)    
    capsule.append(date)       
    
    if entity == "client":
        capsule.append(total_venta) 
    
    return capsule