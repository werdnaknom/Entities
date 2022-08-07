import typing as t
from dataclasses import dataclass, field
import datetime


@dataclass
class ErrorEntity:
    _id = None
    error_traceback: Exception
    error_msg: str
    modified_date: datetime.datetime = field(
        default=datetime.datetime.utcnow(), repr=False, compare=False)
    created_date: datetime.datetime = field(
        default=datetime.datetime.utcnow(), repr=False, compare=False)
