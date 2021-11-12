'''
    Query Validator
'''
import re
from typing import Type

from cherry_ua.assertions import assert_valid


def query_validator(device: Type[str], os_name: Type[str], os_version: Type[str], browser: Type[str], browser_engine: Type[str], browser_version: Type[str], limit: Type[int]):
    str_query_pattern = r'((ne|eq|contains)\(\'[A-z0-9_]+\'\))(((\.(or|and)\.)((ne|eq|contains)\(\'[A-z0-9_]+\'\)))*)'
    int_query_pattern = r'((ne|eq|lte|gte|lt|gt)\(\d+\))(((\.(or|and)\.)((ne|eq|lte|gte|lt|gt)\(\d+\)))*)'
    limit_pattern = r'\d{1,5}'

    assert_valid(re.fullmatch(limit_pattern, str(limit)), 'Invalid Limit value')
    assert_valid(limit > 0  and limit <= 10000, 'Limit should be between 1 and 10000')

    if (device is not None): 
        assert_valid(re.fullmatch(str_query_pattern, device), 'Invalid device query')
    if (os_name is not None):
        assert_valid(re.fullmatch(str_query_pattern, os_name), 'Invalid os query')
    if (os_version is not None):
        assert_valid(re.fullmatch(int_query_pattern, os_version), 'Invalid os version query')
    if (browser is not None):
        assert_valid(re.fullmatch(str_query_pattern, browser), 'Invalid browser query')
    if (browser_engine is not None):
        assert_valid(re.fullmatch(str_query_pattern, browser_engine), 'Invalid browser engine query')
    if (browser_version is not None):
        assert_valid(re.fullmatch(int_query_pattern, browser_version), 'Invalid browser_version query')