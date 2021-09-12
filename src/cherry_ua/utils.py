import platform

def _is_windows():
    if ('win' in platform.system().lower()):
        return True
    return False


