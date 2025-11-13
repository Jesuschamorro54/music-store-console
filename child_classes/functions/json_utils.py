import json
import os
from child_classes.functions.path_utils import get_file_path

def read_json_file(filename):
    file_path = get_file_path(filename)
    if not os.path.exists(file_path):
        return []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                return []
            data = json.loads(content)
            if isinstance(data, list):
                return data
            else:
                return [data]
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Error leyendo archivo {filename}: {e}")
        return []


def write_json_file(filename, data):
    file_path = get_file_path(filename)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error escribiendo archivo {filename}: {e}")


def append_to_json_file(filename, new_data):
    
    existing_data = read_json_file(filename)
    
    existing_data.append(new_data)
    write_json_file(filename, existing_data)


def update_json_file(filename, data_list):
    write_json_file(filename, data_list)