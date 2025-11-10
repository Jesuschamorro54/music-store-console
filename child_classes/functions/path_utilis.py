import os

def get_project_root():
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    project_root = os.path.dirname(os.path.dirname(current_dir))
    
    return project_root


def get_file_path(filename):
    project_root = get_project_root()
    file_path = os.path.join(project_root, "database", filename)
    return file_path