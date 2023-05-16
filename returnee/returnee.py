"""This is a file for all the error codes constants in the application.

Author: buyiyihu
"""

from enum import Enum

from flask import g


class Result(Exception, Enum):
    """A class dedicated to API errors, with a function to create standard
    response data.

    A instance can either be returned or raised. `raise
    Result.BAD_REQUEST_DATA` or `return Result.BAD_REQUEST_DATA()` A pair
    of brackets is a must here!
    """

    GOOD = (0, "So far so good")

    #TODO Support customized type

    # 10xx for improper request
    BAD_REQUEST_DATA = (1000, "Improper request data or parameters")
    MISSING_IMPORTANT_PART = (1001, "Missing or empty data")
    INVALID_DATA_TYPE = (1005, "Invalid data content or type")
    ENTITY_NOT_FOUND = (1006, "Target entity not found")
    ENTITY_DUPLICATION = (1007, "Duplication in request data")
    REQUEST_DATA_CONFLICT = (1008, "Request data conflict")
    INVALID_CONFIG_VALUE = (1020, "Value check failed.")
    ENTITY_ALREADY_EXIST = (1030, "Entity already exists")
    INVALID_VALUE = (1040, "Invalid value")
    UNSUPPORTED_AI_VERSION = (1041, "Unsupported ai version")

    INVALID_HTTP_METHOD = (1050, "Invalid http method")
    INVALID_ROUTE = (1060, "404 Not found,please check the route")


    def __init__(self, code, note):
        self.code = code
        self.note = note

    def __call__(self, detail="", data=None):
        g.response_data = {"detail": detail, "data": data}
        return self

    def __bool__(self):
        return self.code == 0

    @property
    def data(self):
        return {
            "status": self.status,
            "code": self.code,
            "hint": self.hint,
            "data": self.response_data,
        }

    @property
    def response_data(self):
        return g.response_data.get("data")

    @property
    def status(self):
        return "ok" if self.code == 0 else "fail"

    @property
    def hint(self):
        detail = g.response_data.get("detail")
        if self.code != 0:
            detail = self.note + ":\n" + detail if detail else self.note
        return detail

