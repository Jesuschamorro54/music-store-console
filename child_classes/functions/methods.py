from child_classes.functions.validations import *
from child_classes.functions.path_utils import get_file_path
from datetime import datetime


def get_product_by_id(product_id):
    """Busca un producto por su ID en el inventario"""
    from child_classes.functions.json_utils import read_json_file
    products = read_json_file("stocktaking.json")
    
    for product in products:
        if product['id'] == product_id:
            return product
    return None


def get_client_by_id(client_id):
    """Busca un cliente por su ID"""
    from child_classes.functions.json_utils import read_json_file
    clients = read_json_file("client.json")
    
    for client in clients:
        if client['id'] == client_id:
            return client
    return None


def show_cart(carrito, total_venta):
    """Muestra el contenido del carrito de compras"""
    print(f"\n{'='*70}")
    print(f"  {'🛒 CARRITO DE COMPRAS':^66}")
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
    """
    Función mejorada para registrar ventas y compras
    - Ventas: Busca cliente por ID, muestra catálogo y carrito interactivo
    - Compras: Busca proveedor por nombre (actualiza inventario)
    - Fecha automática
    """
    from child_classes.functions.json_utils import read_json_file
    from child_classes.stocks import Stock
    
    sale_file_path = get_file_path("sale.json")
    buys_file_path = get_file_path("buys.json")
    ide = define_id(sale_file_path) if entity == "client" else define_id(buys_file_path)
    product = {}
    capsule = []
    entity_id = None
    
    # === BUSCAR CLIENTE O PROVEEDOR ===
    if entity == "client":
        print("\n=== BUSCAR CLIENTE ===")
        while True:
            try:
                client_id = int(input("|ID Cliente        |: "))
                client = get_client_by_id(client_id)
                if client:
                    entity_id = client_id
                    print(f"✓ Cliente encontrado: {client['name']} {client['last_name']}")
                    break
                else:
                    print("❌ Cliente no encontrado. Intente nuevamente.")
            except ValueError:
                print("❌ Debe ingresar un ID numérico válido")
    else:
        # Para compras, sigue buscando por nombre
        while True:
            name_entity = input("|Proveedor         |: ")
            supplier_file_path = get_file_path("supplier.json")
            valid = validate_exist(supplier_file_path, name_entity)
            if valid[0]:
                entity_id = valid[1]
                print(f"✓ Proveedor encontrado")
                break
            else:
                print("❌ El proveedor no se ha encontrado")

    # === AGREGAR PRODUCTOS AL CARRITO ===
    if entity == "client":
        # Mostrar catálogo para ventas
        stock_ins = Stock()
        stock_ins.show_catalog()
    
    total_venta = 0
    carrito = []
    agregando_productos = True
    
    while agregando_productos:
        print("\n=== AGREGAR PRODUCTOS ===")
        
        while True:
            try:
                producto_id = int(input("|ID Producto       |: "))
                if producto_id == 0:
                    if not carrito:
                        print("❌ Debe agregar al menos un producto")
                        continue
                    agregando_productos = False
                    break
                
                # Buscar producto por ID
                producto = get_product_by_id(producto_id)
                if not producto:
                    print("❌ Producto no encontrado")
                    continue
                
                print(f"✓ Producto: {producto['name']}")
                print(f"  Precio: ${producto.get('precio_venta', 0):,.0f}")
                print(f"  Stock disponible: {producto['lot']} unidades")
                
                # Solicitar cantidad
                while True:
                    try:
                        cantidad = int(input("|Cantidad          |: "))
                        if cantidad <= 0:
                            print("❌ La cantidad debe ser mayor a 0")
                            continue
                        
                        # Validar stock solo para ventas
                        if entity == "client":
                            if cantidad > producto['lot']:
                                print(f"❌ Stock insuficiente. Disponible: {producto['lot']}")
                                continue
                        
                        break
                    except ValueError:
                        print("❌ Debe ingresar un número válido")
                
                # Calcular subtotal
                precio = producto.get('precio_venta', 0) if entity == "client" else producto.get('precio_compra', 0)
                subtotal = precio * cantidad
                
                # Agregar al carrito
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
                
                # === MENÚ DESPUÉS DE AGREGAR PRODUCTO ===
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
                                # Continuar agregando productos
                                break
                            elif opcion == 2:
                                # Mostrar carrito
                                show_cart(carrito, total_venta)
                            elif opcion == 3:
                                # Ir a pagar
                                agregando_productos = False
                                break
                            else:
                                print("❌ Opción inválida")
                        except ValueError:
                            print("❌ Debe ingresar un número válido")
                    
                    if not agregando_productos:
                        break
                else:
                    # Para compras, preguntar si agregar más
                    continuar = input("\n¿Agregar más productos? (s/n): ").lower()
                    if continuar != 's':
                        agregando_productos = False
                        break
                
            except ValueError:
                print("❌ Debe ingresar un ID numérico válido")

    # === PROCESO DE PAGO (SOLO PARA VENTAS) ===
    if entity == "client":
        # Mostrar resumen final
        print(f"\n{'='*70}")
        print(f"  {'💳 RESUMEN FINAL DE LA VENTA':^66}")
        print(f"{'='*70}")
        print(f"  Cliente: {client['name']} {client['last_name']} (ID: {client_id})")
        
        # Fecha automática
        fecha_actual = datetime.now()
        date = fecha_actual.strftime("%Y-%m-%d")
        hora = fecha_actual.strftime("%H:%M:%S")
        
        print(f"  Fecha: {date}")
        print(f"  Hora: {hora}")
        print(f"{'─'*70}")
        
        # Detalle de productos
        print(f"{'CANT':>6}  {'PRODUCTO':<30} {'P.UNIT':>12} {'SUBTOTAL':>14}")
        print(f"{'-'*70}")
        for item in carrito:
            print(f"{item['cantidad']:>6}x  {item['nombre']:<30} "
                  f"${item['precio_unitario']:>10,.0f} ${item['subtotal']:>12,.0f}")
        
        print(f"{'='*70}")
        print(f"{'TOTAL A PAGAR':>52} ${total_venta:>14,.0f}")
        print(f"{'='*70}")
        
        # Confirmar pago
        print("\n¿Confirmar la venta?")
        confirmar = input("[S] Sí - Procesar pago  [N] No - Cancelar: ").lower()
        
        if confirmar != 's':
            print("\n❌ Venta cancelada")
            return None
        
        print("\n✅ Venta procesada exitosamente!")
        print(f"📄 Factura #: {ide}")
        print(f"💰 Total: ${total_venta:,.0f}")
    else:
        # Para compras, fecha automática también
        date = datetime.now().strftime("%Y-%m-%d")

    capsule.append(ide)         # 0: ID de la venta/compra
    capsule.append(entity_id)   # 1: ID del cliente/proveedor
    capsule.append(product)     # 2: Diccionario de productos {nombre: cantidad}
    capsule.append(date)        # 3: Fecha (automática)
    
    if entity == "client":
        capsule.append(total_venta)  # 4: Total de la venta
    
    return capsule
