import random
import math
import numpy as np
import sys
import numexpr as ne
from .agent_filters import *

# import multiprocessing
#
# multiprocessing.set_start_method("fork")


# def save_agents_to_db_sync(timestep, agents):
#     """Синхронная версия save_agents_to_db() для работы в отдельном процессе"""
#     import sqlite3  # Импортировать тут, чтобы избежать проблем с потоками
#
#     conn = sqlite3.connect("/Users/barssoft/Projects/learn_cadcad/agents.db")
#     cursor = conn.cursor()
#
#     data_to_insert = [(timestep, i, *agents[i]) for i in range(len(agents))]
#
#     cursor.executemany(
#         """
#         INSERT INTO agents (timestep, agent_id, param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9, param_10)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
#     """,
#         data_to_insert,
#     )
#
#     conn.commit()
#     conn.close()


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

    # if time_step % 10 == 0:
    #     process = multiprocessing.Process(
    #         target=save_agents_to_db_sync, args=(time_step, previous_state["agents"])
    #     )
    #     process.start()
    #     process.join()

    if len(state_history) > 2:
        state_to_clean = state_history[-3]

        if isinstance(state_to_clean, list):
            for sub_state in state_to_clean:
                if isinstance(sub_state, dict) and "agents" in sub_state:
                    sub_state["agents"] = None

    return {}
