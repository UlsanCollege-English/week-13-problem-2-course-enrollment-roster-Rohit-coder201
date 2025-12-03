import sys
from pathlib import Path

# Ensure the project's root (parent of tests directory) is first on sys.path
# so that `import main` inside tests resolves to this project's `main.py`
project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)
