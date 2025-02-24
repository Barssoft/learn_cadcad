from model.parts.policy_functions import *
from model.parts.state_update_functions import *

import numpy as np

def initialize_seed(params, substep, state_history, previous_state):
    if previous_state['timestep'] == 0:
        np.random.seed(seed=previous_state['simulation']+previous_state['substep']+previous_state["run"])
    return {}



partial_state_update_blocks = [

        #step 0
    {
        'policies': {
            'initialize_seed': initialize_seed,
            

        },
        'variables': {
            #'status': ,

        }
    },



 ]