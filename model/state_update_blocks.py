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
        "policies": {"initialize_seed": initialize_seed, "new_agents": p_new_agents},
        "variables": {"agents": s_new_agents, "number_agents": s_number_agents},
    },
    {
        "policies": {"p_add_balance": p_add_balance},
        "variables": {},
    },
    {
        "policies": {"clean": p_cleanup_objects},
        "variables": {},
    },
]
