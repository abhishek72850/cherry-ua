from requests import Request, Response, PreparedRequest, Session
from typing import Dict, Type

from cherry_ua.decorators import validate_response


class Network(Session):
    def __init__(self):
        super().__init__()

    def __hijack_headers(self, prepared_request: Type[PreparedRequest]) -> Type[PreparedRequest]:
        prepared_request.headers.update({
            'Content-Type': 'application/json'
        })

        return prepared_request

    def get_request(self, url: Type[str], query_params: Type[Dict] = {}, headers: Type[Dict] = {}, **kwargs) -> Type[Dict]:
        request = Request(method='GET', url=url,
                          params=query_params, headers=headers, **kwargs)
        prepared_request = self.__hijack_headers(self.prepare_request(request))
        return self.__get_response(prepared_request).json()

    @validate_response
    def __get_response(self, prepared_request: Type[PreparedRequest], **kwargs) -> Type[Response]:
        return self.send(prepared_request, **kwargs)
