import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def load_db_properties(file_path):
    props = {}
    with open(file_path) as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=")
                props[key.strip()] = value.strip()
    return props
