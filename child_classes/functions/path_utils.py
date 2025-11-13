import os


def get_project_root():
    """
    Obtiene la ruta raíz del proyecto de forma dinámica.
    Busca desde el archivo actual hasta encontrar la carpeta que contiene main.py
    """
    current_file = os.path.abspath(_file_)
    current_dir = os.path.dirname(current_file)
    
    # Subir dos niveles desde child_classes/functions/ hasta la raíz del proyecto
    project_root = os.path.dirname(os.path.dirname(current_dir))
    
    return project_root


def get_file_path(filename):
    """
    Construye la ruta completa a un archivo en la carpeta database/
    
    Args:
        filename: nombre del archivo (ej: 'client.json')
    
    Returns:
        Ruta absoluta al archivo
    """
    project_root = get_project_root()
    file_path = os.path.join(project_root, "database", filename)
    return file_path