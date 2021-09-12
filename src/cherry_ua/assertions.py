from exceptions import CherryException
from typing import List, Dict, Type


def assert_valid(condition: Type[bool], message: Type[str]):
    if not condition: raise CherryException(message)