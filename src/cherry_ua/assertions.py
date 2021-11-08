from typing import Type

from cherry_ua.exceptions import CherryException


def assert_valid(condition: Type[bool], message: Type[str]):
    if not condition: raise CherryException(message)