import os

# Ruta base del proyecto (3 niveles arriba desde este archivo)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILES_DIR = os.path.join(BASE_DIR, "files")

# Archivos JSON del sistema
CLIENT_PATH = os.path.join(FILES_DIR, "client.json")
SUPPLIER_PATH = os.path.join(FILES_DIR, "supplier.json")
STOCK_PATH = os.path.join(FILES_DIR, "stocktaking.json")
SALE_PATH = os.path.join(FILES_DIR, "sale.json")
BUY_PATH = os.path.join(FILES_DIR, "buys.json")
