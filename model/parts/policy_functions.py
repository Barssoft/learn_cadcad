import random
import math
import pandas as pd
import numpy as np
import sys
import numexpr as ne
import numba as nb


def p_start(params, substep, state_history, previous_state):
    return {}


def p_new_agents(params, substep, state_history, previous_state):
    num_new_agents = random.randint(50, 100)

    ranges = np.array(
        [
            (0, 100),
            (50, 200),
            (1, 10),
            (0, 1),
            (100, 500),
            (0, 50),
            (-10, 10),
            (0, 5),
            (10, 100),
            (0, 1),
        ],
        dtype=np.float32,
    )

    new_agents = (
        np.random.rand(num_new_agents, 10) * (ranges[:, 1] - ranges[:, 0])
        + ranges[:, 0]
    )

    return {"new_agents": new_agents}


@nb.njit(parallel=True)
def fast_update(agents, active_size):
    for i in nb.prange(active_size):
        if agents[i, 2] > 2:
            agents[i, 0] += 10


def p_add_balance(params, substep, state_history, previous_state):
    ne.set_num_threads(ne.ncores)
    agents = previous_state["agents"]
    active_size = previous_state["number_agents"]

    fast_update(agents, active_size)

    # col2 = agents[:active_size, 2]
    # agents[:active_size, 0] += ne.evaluate("10 * (col2 > 2)")

    return {}


def p_cleanup_objects(params, substep, state_history, previous_state):
    time_step = previous_state["timestep"]
    if time_step % 1000 == 0:
        print(f"step is gone {time_step}")

    if len(state_history) > 2:
        try:
            state_to_clean = state_history[-3]
            if isinstance(state_to_clean, list):
                for sub_state in state_to_clean:
                    if isinstance(sub_state, dict):
                        for obj_name in ["agents"]:
                            if obj_name in sub_state:
                                sub_state[obj_name] = None

        except (IndexError, TypeError, KeyError) as e:
            print("Ошибка при обработке истории:", e)

    return {}
