
def s_start(params, substep, state_history, previous_state, policy_input):

    updated = previous_state['start'] + 1
    return 'start', updated
