from model.parts.policy_functions import *
from model.parts.state_update_functions import *


def initialize_seed(params, substep, state_history, prev_state):
    if prev_state["timestep"] == 0:
        random.seed(
            a=f'{prev_state["simulation"]}/{prev_state["subset"]}/{prev_state["run"]}/{prev_state["timestep"]}'
        )
    return {}


partial_state_update_blocks = [
    {
        "policies": {
            "initialize_seed": initialize_seed,
        },
        "variables": {"start": s_start},
    },
]
