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
- **Control de Inventario**: Registro y consulta de stock de productos
- **Sistema de Ventas**: Registro de ventas con validación de stock
- **Sistema de Compras**: Gestión de compras a proveedores
- **Consultas Avanzadas**: Búsqueda por fechas, facturas e IDs
- **Interfaz de Consola**: Menú intuitivo con colores y navegación fácil
- **Persistencia de Datos**: Almacenamiento en archivos JSON

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
│       └── validations.py     # Validaciones de datos
└── files/                     # Archivos de persistencia
    ├── client.json             # Datos de clientes
    ├── supplier.json           # Datos de proveedores
    ├── sale.json               # Registro de ventas
    ├── buys.json               # Registro de compras
    └── stocktaking.json        # Inventario de productos
```

## 🚀 Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Jesuschamorro54/music-store-console.git
   cd music-store-console
   ```

2. **Instala las dependencias:**
   ```bash
   pip install pyautogui
   ```

3. **Ejecuta la aplicación:**
   ```bash
   python main.py
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
|  5. REGISTRAR INVENTARIO   0. SALIR                        |
```

## 🔧 Funcionalidades

### 📝 Registro de Entidades
- **Clientes**: ID, nombre, apellido, email, teléfono
- **Proveedores**: ID, nombre, email, teléfono
- **Productos**: ID, nombre, cantidad en stock

### 💰 Sistema de Transacciones
- **Ventas**: Registro de ventas con validación de stock disponible
- **Compras**: Gestión de compras a proveedores
- **Actualización automática**: El stock se actualiza automáticamente con cada transacción

### 🔍 Consultas y Reportes
- **Ventas por rango de fechas**: Consulta de ventas entre dos fechas específicas
- **Venta por factura**: Búsqueda de venta específica por ID
- **Consulta de cliente**: Búsqueda por ID y nombre
- **Consulta de inventario**: Verificación de stock por ID de producto

### ✅ Validaciones
- **Validación de email**: Verificación de formato de correo electrónico
- **Validación de fechas**: Formato de fecha correcto (YYYY-MM-DD)
- **Validación de stock**: Verificación de disponibilidad antes de ventas
- **Validación de entidades**: Verificación de existencia de clientes y proveedores

## 🛠️ Tecnologías

- **Python 3.x**: Lenguaje de programación principal
- **JSON**: Formato de almacenamiento de datos
- **PyAutoGUI**: Automatización de interfaz (opcional)
- **Programación Orientada a Objetos**: Arquitectura basada en clases

## 🏗️ Arquitectura

### Patrón de Diseño
El proyecto utiliza el patrón de **Herencia** con las siguientes clases:

- **`Entity`**: Clase padre para operaciones básicas de archivos
- **`Facture`**: Clase padre para transacciones comerciales
- **Clases hijas**: `Client`, `Supplier`, `Sale`, `Buy`, `Stock`

### Principios SOLID
- **Responsabilidad única**: Cada clase tiene una responsabilidad específica
- **Herencia**: Reutilización de código mediante herencia
- **Encapsulación**: Uso de propiedades y métodos privados

### Persistencia de Datos
- **Formato JSON**: Almacenamiento estructurado en archivos de texto
- **Separación por entidad**: Un archivo por cada tipo de dato
- **Operaciones CRUD**: Create, Read, Update implícitas

## 📊 Flujo de Trabajo

1. **Registro inicial**: Se registran proveedores y productos en inventario
2. **Gestión de clientes**: Registro de clientes para futuras ventas
3. **Operaciones comerciales**: Realización de ventas y compras
4. **Consultas**: Verificación de datos y reportes

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
