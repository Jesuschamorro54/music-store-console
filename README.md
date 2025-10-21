# 🎵 Music Store Console

Un sistema de gestión de tienda de instrumentos musicales desarrollado en Python con programación orientada a objetos. Esta aplicación de consola permite administrar clientes, proveedores, inventario, ventas y compras de manera eficiente.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Funcionalidades](#-funcionalidades)
- [Tecnologías](#-tecnologías)
- [Arquitectura](#-arquitectura)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

## ✨ Características

- **Gestión de Clientes**: Registro y consulta de información de clientes
- **Gestión de Proveedores**: Administración de proveedores de instrumentos
- **Control de Inventario**: Consulta de stock de productos con precios y ganancias
- **Sistema de Ventas Mejorado**:
  - 🔍 Búsqueda de clientes por ID
  - 📋 Catálogo interactivo de productos con precios
  - 🛒 Carrito de compras interactivo con selección por ID
  - 👁️ Opción "Ver carrito" en cualquier momento
  - 💳 Opción "Ir a pagar" para finalizar compra
  - 💰 Cálculo automático de totales y subtotales
  - 📅 Fecha y hora automática (sin entrada manual)
  - 📊 Resumen detallado con confirmación de pago
  - ✅ Validación de stock en tiempo real
  - ❌ Opción de cancelar venta antes de confirmar
- **Gestión de Precios**:
  - Precio de compra y venta por producto
  - Cálculo automático de ganancias y porcentajes
  - Control de márgenes de ganancia
- **Sistema de Compras**: Gestión de compras a proveedores (actualiza automáticamente el inventario)
- **Consultas Avanzadas**: Búsqueda por fechas, facturas e IDs
- **Interfaz de Consola**: Menú intuitivo con colores y navegación fácil
- **Persistencia de Datos**: Almacenamiento en archivos JSON
- **Rutas Dinámicas**: Sistema compatible con cualquier dispositivo sin necesidad de cambiar rutas

## 📁 Estructura del Proyecto

```
music-store-console/
├── main.py                     # Archivo principal con el menú de navegación
├── parent_classes/             # Clases padre
│   ├── entity_class.py        # Clase base para entidades
│   └── facture_class.py       # Clase base para facturas
├── child_classes/             # Clases hijas especializadas
│   ├── client_class.py        # Gestión de clientes
│   ├── supplier_class.py      # Gestión de proveedores
│   ├── sale_class.py          # Gestión de ventas
│   ├── buys_class.py          # Gestión de compras
│   ├── stocks.py              # Gestión de inventario
│   └── functions/             # Funciones auxiliares
│       ├── methods.py         # Métodos de entrada de datos
│       ├── validations.py     # Validaciones de datos
│       ├── path_utils.py      # Utilidades para rutas dinámicas
│       └── json_utils.py      # Utilidades para manejo de archivos JSON
└── database/                  # Archivos de persistencia (JSON)
    ├── client.json            # Datos de clientes
    ├── supplier.json          # Datos de proveedores
    ├── sale.json              # Registro de ventas (con totales)
    ├── buys.json              # Registro de compras
    └── stocktaking.json       # Inventario con precios y stock
```

## 🚀 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Jesuschamorro54/music-store-console.git
   cd music-store-console
   ```

2. **Requisitos:**
   - Python 3.x (no requiere dependencias externas, solo módulos nativos)

3. **Ejecuta la aplicación:**
   ```bash
   python3 main.py
   ```

## 🎮 Uso

Al ejecutar la aplicación, aparecerá un menú interactivo con las siguientes opciones:

```
-- COMPRA Y VENTA DE INSTRUMENTOS MUSICALES --

__________________________________________________________________
-----------------------------| MENU |-----------------------------
        
|  1. REGISTRAR CLIENTE      6. CONSULTAR VENTAS POR FECHAS  |
|  2. REGISTRAR PROVEEDOR    7. CONSULTAR VENTA POR FACTURA  |
|  3. REGISTRAR VENTA        8. CONSULTAR CLIENTE            |
|  4. REGISTRAR COMPRAS      9. CONSULTAR INVENTARIO         |
|                            0. SALIR                        |
```

## 🔧 Funcionalidades

### 📝 Registro de Entidades
- **Clientes**: ID, nombre, apellido, email, teléfono
- **Proveedores**: ID, nombre, email, teléfono
- **Productos**: ID, nombre, stock, precio de compra, precio de venta
  - Cálculo automático de ganancias por producto
  - Control de inventario en tiempo real

### 💰 Sistema de Transacciones

**Ventas Mejoradas:**
- Búsqueda de clientes por ID (más rápido y preciso)
- Visualización de catálogo completo con precios
- Selección de productos por ID
- **Menú interactivo después de cada producto:**
  - [1] Agregar más productos
  - [2] Ver carrito actual
  - [3] Ir a pagar
- Carrito de compras visible en cualquier momento
- Validación de stock en tiempo real
- Cálculo automático de subtotales y total
- **Fecha y hora automática del sistema**
- Resumen final detallado con información del cliente
- Confirmación de pago antes de procesar
- Opción de cancelar la venta
- Registro de venta con total incluido

**Compras:**
- Búsqueda de proveedores por nombre
- Gestión de compras a proveedores
- Actualización automática de inventario
- Control de precios de compra

**Automatización:**
- El stock se actualiza automáticamente con cada transacción
- Cálculo de ganancias por venta
- Control de márgenes de ganancia

### 🔍 Consultas y Reportes
- **Ventas por rango de fechas**: Consulta de ventas entre dos fechas específicas
- **Venta por factura**: Búsqueda de venta específica por ID
- **Consulta de cliente**: Búsqueda por ID y nombre
- **Consulta de inventario**: Verificación de stock por ID de producto

### ✅ Validaciones
- **Validación de ID**: Verificación de entrada numérica válida (método heredado)
- **Validación de email**: Verificación de formato correo electrónico con @ y dominio (método heredado)
- **Validación de teléfono**: Verificación de número con mínimo 7 dígitos (método heredado)
- **Validación de campos**: Prevención de campos vacíos en nombres
- **Validación de fechas**: Formato de fecha correcto (YYYY-MM-DD)
- **Validación de stock**: Verificación de disponibilidad antes de ventas
- **Validación de entidades**: Verificación de existencia de clientes y proveedores

## 🛠️ Tecnologías

- **Python 3.x**: Lenguaje de programación principal
- **JSON**: Formato estándar de almacenamiento de datos (RFC 8259)
- **Programación Orientada a Objetos**: 
  - Herencia de clases
  - Polimorfismo (métodos sobrescritos)
  - Encapsulación (propiedades y métodos privados)
  - Abstracción (métodos base en clases padre)
- **Módulos nativos**: `json`, `os`, `sys` para funcionalidad del sistema

## 🏗️ Arquitectura

### Patrón de Diseño
El proyecto utiliza el patrón de **Herencia y Polimorfismo** con las siguientes clases:

```
┌─────────────────────────────────────┐
│          Entity (Padre)             │
├─────────────────────────────────────┤
│ + write_into()                      │
│ + read_file()                       │
│ + _validate_id()                    │
│ + _validate_email()                 │
│ + _validate_phone()                 │
│ + capture_data() [abstracto]        │
└─────────────────────────────────────┘
            ▲           ▲
            │           │
     ┌──────┴───┐   ┌───┴──────┐
     │          │   │          │
┌────┴────┐ ┌───┴───┴─┐  ┌────┴────┐
│ Client  │ │Supplier │  │  Stock  │
├─────────┤ ├─────────┤  └─────────┘
│capture_ │ │capture_ │
│data()   │ │data()   │
│(5 datos)│ │(4 datos)│
└─────────┘ └─────────┘

┌─────────────────────────────────────┐
│         Facture (Padre)             │
├─────────────────────────────────────┤
│ + write_into()                      │
│ + read_file()                       │
│ + update_stock()                    │
└─────────────────────────────────────┘
            ▲           ▲
            │           │
     ┌──────┴───┐   ┌───┴──────┐
     │          │   │          │
  ┌──┴──┐    ┌──┴──┐
  │Sale │    │ Buy │
  └─────┘    └─────┘
```

- **`Entity`**: Clase padre para operaciones básicas de archivos y validaciones
  - Métodos de validación: `_validate_id()`, `_validate_email()`, `_validate_phone()`
  - Método abstracto: `capture_data()` (debe ser implementado por clases hijas)
- **`Facture`**: Clase padre para transacciones comerciales
- **Clases hijas**: `Client`, `Supplier`, `Sale`, `Buy`, `Stock`

### Principios SOLID y POO
- **Responsabilidad única**: Cada clase tiene una responsabilidad específica
- **Herencia**: Reutilización de código mediante herencia de clases padre
- **Polimorfismo**: Las clases `Client` y `Supplier` implementan su propia versión de `capture_data()`
  - `Client.capture_data()`: Captura ID, nombre, apellido, email y teléfono
  - `Supplier.capture_data()`: Captura ID, nombre, email y teléfono (sin apellido)
- **Encapsulación**: Uso de propiedades, métodos privados y getters/setters
- **Abstracción**: Métodos base en la clase padre que las clases hijas deben implementar

### Ejemplo de Polimorfismo en Acción

```python
# En main.py - Mismo código, diferente comportamiento

# Registrar Cliente (polimorfismo)
client_ins = Client()
data = client_ins.capture_data()  # Captura 5 datos
client_ins.client = data

# Registrar Proveedor (polimorfismo)
supplier_ins = Supplier()
data = supplier_ins.capture_data()  # Captura 4 datos
supplier_ins.supplier = data

# Ambos usan el mismo método capture_data(), 
# pero cada clase lo implementa de forma diferente
```

**Ventajas del enfoque POO implementado:**
- ✅ Elimina código procedural y funciones independientes
- ✅ Cada entidad es responsable de capturar sus propios datos
- ✅ Las validaciones se reutilizan mediante herencia
- ✅ Fácil extensión para nuevas entidades
- ✅ Código más mantenible y legible

### Persistencia de Datos
- **Formato JSON estándar**: Almacenamiento en arrays JSON válidos (RFC 8259)
- **Separación por entidad**: Un archivo por cada tipo de dato
- **Rutas dinámicas**: Sistema de rutas relativas que funciona en cualquier dispositivo
- **Operaciones CRUD**: Create, Read, Update implementadas con funciones especializadas
- **Lectura/Escritura optimizada**: Funciones centralizadas en `json_utils.py` para manejo consistente de datos

## 📊 Flujo de Trabajo

1. **Registro inicial**: Se registran proveedores
2. **Gestión de clientes**: Registro de clientes para futuras ventas
3. **Gestión de inventario**: Se debe registrar el stock inicial mediante compras a proveedores
4. **Operaciones comerciales**: Realización de ventas y compras
5. **Consultas**: Verificación de datos y reportes

## 🛍️ Ejemplo de Proceso de Venta Mejorado

```
=== BUSCAR CLIENTE ===
|ID Cliente        |: 123
✓ Cliente encontrado: jesus chamorro

================================================================================
                              CATÁLOGO DE PRODUCTOS
================================================================================
ID    PRODUCTO                  STOCK      P.VENTA         DISPONIBLE
--------------------------------------------------------------------------------
10    clarinete                 77         $  1,121,000    ✓ Disponible
11    trombon                   50         $  1,700,000    ✓ Disponible
12    trompeta                  162        $    583,000    ✓ Disponible
...
================================================================================

=== AGREGAR PRODUCTOS ===
|ID Producto       |: 10
✓ Producto: clarinete
  Precio: $1,121,000
  Stock disponible: 77 unidades
|Cantidad          |: 2

✓ Agregado: 2x clarinete = $2,242,000

──────────────────────────────────────────────────
  [1] Agregar más productos
  [2] Ver carrito
  [3] Ir a pagar
──────────────────────────────────────────────────
Seleccione una opción: 2

======================================================================
                         🛒 CARRITO DE COMPRAS                       
======================================================================
  CANT  PRODUCTO                             P.UNIT       SUBTOTAL
----------------------------------------------------------------------
     2x  clarinete                      $ 1,121,000 $   2,242,000
======================================================================
                                       TOTAL A PAGAR $   2,242,000
======================================================================

──────────────────────────────────────────────────
  [1] Agregar más productos
  [2] Ver carrito
  [3] Ir a pagar
──────────────────────────────────────────────────
Seleccione una opción: 1

|ID Producto       |: 12
✓ Producto: trompeta
  Precio: $583,000
  Stock disponible: 162 unidades
|Cantidad          |: 1

✓ Agregado: 1x trompeta = $583,000

──────────────────────────────────────────────────
  [1] Agregar más productos
  [2] Ver carrito
  [3] Ir a pagar
──────────────────────────────────────────────────
Seleccione una opción: 3

======================================================================
                      💳 RESUMEN FINAL DE LA VENTA                   
======================================================================
  Cliente: jesus chamorro (ID: 123)
  Fecha: 2025-10-20
  Hora: 23:10:24
──────────────────────────────────────────────────────────────────────
  CANT  PRODUCTO                             P.UNIT       SUBTOTAL
----------------------------------------------------------------------
     2x  clarinete                      $ 1,121,000 $   2,242,000
     1x  trompeta                       $   583,000 $     583,000
======================================================================
                                       TOTAL A PAGAR $   2,825,000
======================================================================

¿Confirmar la venta?
[S] Sí - Procesar pago  [N] No - Cancelar: s

✅ Venta procesada exitosamente!
📄 Factura #: 202
💰 Total: $2,825,000
```

## 🔄 Actualizaciones del Sistema

- **Stock automático**: Las ventas reducen automáticamente el inventario
- **Compras**: Las compras incrementan el stock disponible
- **Validaciones en tiempo real**: Verificación de disponibilidad antes de transacciones

## 🤝 Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Jesús Chamorro**
- GitHub: [@Jesuschamorro54](https://github.com/Jesuschamorro54)

## 📞 Soporte

Si tienes alguna pregunta o sugerencia, no dudes en:
- Abrir un [Issue](https://github.com/Jesuschamorro54/music-store-console/issues)
- Contactar al desarrollador

---

⭐ ¡No olvides dar una estrella al proyecto si te resulta útil!
