import typing as t
from dataclasses import dataclass, field
import collections

from ..requests import RequestObject, ValidRequestObject, InvalidRequestObject


class WebProcessingRequestObject(ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return WebProcessingRequestObject(filters=adict.get('filters', None))
