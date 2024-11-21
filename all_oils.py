import os
import importlib.util



def get_all_oils_in_folder( folder_path):
    # Define the folder containing the Python files
    python_files = [file for file in os.listdir(folder_path) if file.endswith(".py")]
    # Iterate over each Python file
    all_objects = []
    for file_name in python_files:
        # Get the module name
        module_name = os.path.splitext(file_name)[0]

        # Import the module dynamically
        module_spec = importlib.util.spec_from_file_location(module_name, os.path.join(folder_path, file_name))
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)

        # Get all classes defined in the module
        classes = [obj for obj in module.__dict__.values() if isinstance(obj, type)]

        # Instantiate objects of each class
        for class_ in classes:
            # Check if the class is not a module, and if it's not a private class (starting with "_")
            if class_.__module__ == module_name and not class_.__name__.startswith("_"):
                instance = class_()
                all_objects.append(instance)
    return all_objects


def get_all_oils():
    folder_path = ["oils", 'oils/Citrus']
    # Get a list of Python files in the folder
    all_oils = []
    for folder in folder_path:
        all_oils += get_all_oils_in_folder(folder)

    return all_oils

if __name__ == "__main__":
    get_all_oils()