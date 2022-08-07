import typing as t
from dataclasses import dataclass, field, asdict
import datetime


@dataclass
class ErrorEntity:
    _id = None
    error_traceback: str
    error_msg: str
    path: str = None
    modified_date: datetime.datetime = field(
        default=datetime.datetime.utcnow(), repr=False, compare=False)
    created_date: datetime.datetime = field(
        default=datetime.datetime.utcnow(), repr=False, compare=False)
    _type: str = "ERROR"

    @classmethod
    def get_type(cls) -> str:
        return cls._type

    def to_mongo(self) -> dict:
        return asdict(self)

    @classmethod
    def from_mongo(cls, adict):
        return cls(**adict)
