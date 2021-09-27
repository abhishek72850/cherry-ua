from functools import wraps

from cherry_ua.assertions import assert_valid


def validate_response(func):
    @wraps(func)
    def wrapping(*args, **kwargs):
        response = func(*args, **kwargs)
        assert_valid(response.status_code == 200, 'API error')
        return response
    return wrapping