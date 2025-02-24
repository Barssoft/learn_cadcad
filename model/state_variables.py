from dataclasses import dataclass, field
from typing import List

@dataclass
class StateVariables:
    
    start: int = 0

initial_state = StateVariables().__dict__

