from dataclasses import dataclass, field
from typing import List
import numpy as np


@dataclass
class StateVariables:

    number_agents: int = 0
    agents: np.ndarray = field(default_factory=lambda: np.empty((0, 10)))


initial_state = StateVariables().__dict__
