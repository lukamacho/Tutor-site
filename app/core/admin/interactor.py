from dataclasses import dataclass
from enum import Enum
from typing import List, Protocol

from result import Err, Ok, Result


class AdminError(Enum):
    INCORRECT_ADMIN_KEY = 0


ADMIN_KEY = "sezam-gaighe"
