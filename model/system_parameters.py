from dataclasses import dataclass
from typing import List
from model.utils import default


@dataclass
class Parameters:
    start: List[int] = default([1])


parameters = Parameters().__dict__
