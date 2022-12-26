import sys

from .app import App

from . import widgets

from . import beatle
from . import sound
from .game_gui_controller import GameGUIController
from . import errors
from .constants import *

if not (sys.version_info.major == 3 and sys.version_info.minor >= 10):  # Версия Python должна быть >= 3.10
    raise errors.VersionError('Версия Python должна быть >= 3.10')

__version__ = '0.2.1'

print(f'\n[Pyne] version -> {__version__}')
