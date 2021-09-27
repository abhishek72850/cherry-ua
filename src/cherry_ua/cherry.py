import json
import os
import random
from types import MethodType
from typing import Dict, List, Type

from cherry_ua.constants import UA
from cherry_ua.network import Network
from cherry_ua.validator import query_validator


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

        self.__set_paths()
        self.__initialize()

    def refresh(self):
        self._ua_list = self.__download_ua()
        self.__save_ua_filters()
        self.__save_ua_db()

    def get_random(self):
        return random.choice(self._ua_list)

    def set_search_filters(self, **kwargs):
        for key, value in kwargs:
            self.__setattr__('_{}'.format(key), value)

    def get_all_filters(self):
        return self.__build_search_params()

    def get(self, filter_name):
        return self.__getattribute__('_{}'.format(filter_name))

    def set(self, filter_name, value):
        self.__setattr__('_{}'.format(filter_name), value)

    def size(self):
        return len(self._ua_list)

    def __initialize(self):
        if (not self.__is_local_db_exist()):
            self.refresh()
        else:
            self.__load_or_download_ua()

    def __set_paths(self):
        self._ua_path = UA.UA_LOCAL_DB_STORAGE_PATH
        self._ua_filters_path = UA.UA_SAVED_FILTER_PATH

    def __load_or_download_ua(self):
        if (self.__is_filter_changed()):
            self.refresh()
        else:
            self.__load_ua_db()

    def __is_filter_changed(self):
        changed = False
        with open(self._ua_filters_path, 'r') as file:
            filters = json.load(file)

            if (filters['device'] != self._device):
                changed = True
            if (filters['os_name'] != self._device):
                changed = True
            if (filters['os_version'] != self._device):
                changed = True
            if (filters['browser'] != self._device):
                changed = True
            if (filters['browser_engine'] != self._device):
                changed = True
            if (filters['browser_version'] != self._device):
                changed = True

        return changed

    def __load_ua_db(self):
        with open(self._ua_path, 'r') as file:
            self._ua_list = json.load(file)

    def __save_ua_db(self):
        with open(self._ua_path, 'w') as file:
            json.dump(self._ua_list, file)

    def __save_ua_filters(self):
        with open(self._ua_filters_path, 'w') as file:
            json.dump(self.__build_search_params(), file)

    def __is_local_db_exist(self):
        return os.path.exists(self._ua_path)

    def __download_ua(self):
        query_params = self.__build_search_params()
        api_data = self.get_request(url=UA.UA_API, query_params=query_params)

        return api_data['data']

    def __build_search_params(self):
        params = {
            'device': self._device,
            'os_name': self._os_name,
            'os_version': self._os_version,
            'browser': self._browser,
            'browser_engine': self._browser_engine,
            'browser_version': self._browser_version,
            'limit': self._limit
        }

        query_validator(**params)

        return params
