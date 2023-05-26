import typing as t
from typing import Optional
import collections
from dataclasses import dataclass, field

from ..requests import RequestObject, ValidRequestObject, InvalidRequestObject


class WebAppProcessingRequest(ValidRequestObject):

    def __init__(self, filters=None):
        self.filters = filters

    @classmethod
    def from_dict(cls, adict):
        invalid_req = InvalidRequestObject()

        if 'filters' in adict and not isinstance(adict['filters'], collections.Mapping):
            invalid_req.add_error('filters', 'Is not iterable')

        if invalid_req.has_errors():
            return invalid_req

        return WebAppProcessingRequest(filters=adict.get('filters', None))


@dataclass
class TestpointInfoRequestObject(RequestObject):
    product: str
    testpoint: str
    test_category: str
    runid_status: Optional[t.List[str]] = field(default_factory=lambda: ["Complete"])
    runid: Optional[t.List[str]] = None
    pba: Optional[str] = None
    environment: Optional[dict] = None


@dataclass
class RunidInfoRequestObject(RequestObject):
    product: str
    runid: int
    test_category: str
    runid_status: t.List[str] = field(default_factory=lambda: ["Complete"])
    temperature: t.Optional[int] = None
    voltages: t.Optional[dict] = None
    testpoints: t.Optional[dict] = None
    optional_values: t.List[str] = field(default_factory=lambda: ["temperature", "testpoints", "voltages"])

    def to_dict(self) -> t.Dict:
        adict = {
            "product": self.product,
            "runid": self.runid,
            "test_category": self.test_category,
            "runid_status": self.runid_status
        }
        for optional in self.optional_values:
            attr = self.__getattribute__(name=optional)
            if attr:
                adict[optional] = attr
        return adict

    def match_query(self) -> t.Dict:
        return {
            "project": self.product,
            "runid": self.runid,
            "status.status": {"$in": self.runid_status}
        }


@dataclass
class TestpointQueryRequestObject(RequestObject):
    product: str
    testpoints: t.Optional[str] = None

    def to_dict(self) -> t.Dict:
        adict = {
            "product": self.product
        }
        if self.testpoints:
            adict["testpoints"] = self.testpoints
        return adict

    def match_query(self) -> t.Dict:
        adict = {
            "product": self.product,
        }
        if self.testpoints:
            adict["testpoint"] = {"$in": self.testpoints}
        return adict
