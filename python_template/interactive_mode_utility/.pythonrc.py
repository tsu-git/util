import sys
from pathlib import Path

interactive_mode_utility = Path('/c/Users/tsusu/source/repos/python_template/interactive_mode_utility')
sys.path.append(str(interactive_mode_utility))

from interactive_mode_utility import find_attr
