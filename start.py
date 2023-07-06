import os

filename = "structure.txt"
base_path = "."  # change this if you want to create files in a specific directory

with open(filename, 'r') as file:
    for line in file:
        indent_count = len(line) - len(line.lstrip())
        level = indent_count // 4  # Assuming an indentation of 4 spaces.
        name = line.strip()

        # If the name contains a ".", assume it's a file; otherwise, assume it's a directory.
        if '.' in name:
            # File
            dir_path = os.path.join(base_path, *name.split('/')[:-1])
            os.makedirs(dir_path, exist_ok=True)
            with open(os.path.join(base_path, *name.split('/')), 'w') as _:
                pass
        else:
            # Directory
            os.makedirs(os.path.join(
                base_path, *name.split('/')), exist_ok=True)
