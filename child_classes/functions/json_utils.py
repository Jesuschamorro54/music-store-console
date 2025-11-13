import json
import os
from child_classes.functions.path_utils import get_file_path


def read_json_file(filename):
    """
    Lee un archivo JSON y retorna su contenido como lista.
    Si el archivo no existe o está vacío, retorna una lista vacía.
    
    Args:
        filename: nombre del archivo (ej: 'client.json')
    
    Returns:
        Lista con los datos del archivo JSON
    """
    file_path = get_file_path(filename)
    
    # Si el archivo no existe, retornar lista vacía
    if not os.path.exists(file_path):
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            # Si el archivo está vacío, retornar lista vacía
            if not content:
                return []
            data = json.loads(content)
            # Asegurar que siempre retorna una lista
            if isinstance(data, list):
                return data
            else:
                return [data]
    except json.JSONDecodeError:
        # Si hay error al leer JSON, retornar lista vacía
        return []
    except Exception as e:
        print(f"Error leyendo archivo {filename}: {e}")
        return []


def write_json_file(filename, data):
    """
    Escribe datos en un archivo JSON con formato correcto.
    
    Args:
        filename: nombre del archivo (ej: 'client.json')
        data: lista de datos a escribir
    """
    file_path = get_file_path(filename)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error escribiendo archivo {filename}: {e}")


def append_to_json_file(filename, new_data):
    """
    Agrega un nuevo registro a un archivo JSON.
    
    Args:
        filename: nombre del archivo (ej: 'client.json')
        new_data: diccionario con el nuevo registro
    """
    # Leer datos existentes
    existing_data = read_json_file(filename)
    
    # Agregar nuevo registro
    existing_data.append(new_data)
    
    # Escribir todos los datos
    write_json_file(filename, existing_data)


def update_json_file(filename, data_list):
    """
    Actualiza completamente un archivo JSON con una nueva lista de datos.
    
    Args:
        filename: nombre del archivo (ej: 'stocktaking.json')
        data_list: lista completa de datos
    """
    write_json_file(filename, data_list)