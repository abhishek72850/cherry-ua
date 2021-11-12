import platform
from typing import Type

def _is_windows() -> Type[bool]:
    if ('win' in platform.system().lower()):
        return True
    return False


