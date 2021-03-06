# -*- coding: utf-8 -*-

# TM1py Exceptions are defined here
from typing import Mapping


class TM1pyTimeout(Exception):
    def __init__(self, method: str, url: str, timeout: float):
        self.method = method
        self.url = url
        self.timeout = timeout

    def __str__(self):
        return f"Timeout after {self.timeout} seconds for '{self.method}' request with url :'{self.url}'"


class TM1pyException(Exception):
    """ The default exception for TM1py

    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class TM1pyRestException(TM1pyException):
    """ Exception for failing REST operations

    """

    def __init__(self, response: str, status_code: int, reason: str, headers: Mapping):
        super(TM1pyRestException, self).__init__(response)
        self._status_code = status_code
        self._reason = reason
        self._headers = headers

    @property
    def status_code(self):
        return self._status_code

    @property
    def reason(self):
        return self.reason

    @property
    def response(self):
        return self.message

    @property
    def headers(self):
        return self._headers

    def __str__(self):
        return "Text: {} Status Code: {} Reason: {} Headers: {}".format(
            self.message,
            self._status_code,
            self._reason,
            self._headers)
