import os
import random

from types import MethodType
from typing import List, Dict, Type

import utils as Utility
from network import Network
from constants import UA, UaFilters


class UserAgent(Network):
    def __init__(
        self,
        device: Type[str] = None,
        os_name: Type[str] = None,
        os_version: Type[str] = None,
        browser: Type[str] = None,
        browser_engine: Type[str] = None,
        browser_version: Type[str] = None,
        limit: Type[int] = 1000,
        **kwargs
    ):
        super().__init__()

        self._device = device
        self._os_name = os_name
        self._os_version = os_version
        self._browser = browser
        self._browser_engine = browser_engine
        self._browser_version = browser_version
        self._limit = limit

    def refresh(self):
        pass

    def get_random(self):
        return random.choice(self._ua_list)

    def __save_ua_db(self):
        tmp_path = '/tmp'

        if (Utility._is_windows()):
            tmp_path = ''
        
        file_name
        
        with open()

    def __is_local_db_exist(self):
        pass

    def __download_ua(self):
        query_params = self.__build_search_params()
        api_data = self.get(url=UA.UA_API, query_params=query_params)

        return api_data
    
    def __build_search_params(self):
        params = {
            'device': self._device,
            'os': self._os_name,
            'os_version': self._os_version,
            'browser': self._browser,
            'browser_engine': self._browser_engine,
            'browser_version': self._browser_version
        }

        return params



