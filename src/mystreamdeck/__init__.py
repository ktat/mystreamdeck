from inspect import isclass
from pkgutil import iter_modules,extend_path
from pathlib import Path
from importlib import import_module
import re

# iterate through the modules in the current package
package_dir = extend_path(__path__, __name__)

for item in iter_modules(package_dir):
    module_name = item.name
    # import the module and iterate through its attributes
    module = import_module(f"{__name__}.{module_name}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        if isclass(attribute):
            # Add the class to this package's variables
            globals()[attribute_name] = attribute

# for mypy: cannot use dynamic loading with mypy
from ._base import *
from ._base_app import *
from .alert import *
from .calendar import *
from .clock import *
from .game_memory import *
from .game_random_number import *
from .game_tic_tack_toe import *
from .game_whac_a_mole import *
from .stop_watch import *
from .weather_jp import *
from .window_check_base import *
from .window_check_linux import *
