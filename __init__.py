import sys, os, inspect
library_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) # script of __init__.py directory

if library_dir not in sys.path:
    sys.path.append(library_dir)
