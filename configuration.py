import os
from sys import argv

data_dir = argv[1] if len(argv) > 1 else "data"

os.makedirs(data_dir, exist_ok=True)
