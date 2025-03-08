import numpy as np
import pandas as pd


def s_number_agents(params, substep, state_history, previous_state, policy_input):
    new_agents = policy_input["new_agents"]
    updated = previous_state["number_agents"] + new_agents.shape[0]
    return "number_agents", updated


def s_new_agents(params, substep, state_history, previous_state, policy_input):
    new_agents = policy_input["new_agents"]
    old_agents = previous_state["agents"]
    start = previous_state["number_agents"]

    if old_agents.shape[0] == 0:
        old_agents = np.empty((2_000_000, 10), dtype=np.float32)

    num_new = new_agents.shape[0]
    old_agents[start : start + num_new] = new_agents

    return "agents", old_agents


def s_clear(params, substep, state_history, previous_state, policy_input):
    if len(state_history) > 2:
        state_history[-3]["agents"] = []

    return "agents", previous_state["agents"]
