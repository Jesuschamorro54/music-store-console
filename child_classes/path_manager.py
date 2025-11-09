import os
# este modulo se encarga de hacer las rutas dinamicas, 
# basicamente da una ruta definida principalmente aqui, para que los modulos 
# importen esta funcion para la busqueda de la carpeta file y losa rchivos correspondientes
def get_file_path(filename):
    # Subir un nivel desde child_classes hasta la carpeta principal
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "files", filename)
    return file_path
