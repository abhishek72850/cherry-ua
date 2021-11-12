'''
    Cherry exceptions module
'''
from typing import Type


class CherryException(Exception):
    def __init__(self, message: Type[str]=""):
        self.message = message
        super().__init__(self.message)
