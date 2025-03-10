import numba as nb
import numpy as np


@nb.njit(parallel=True)
def fast_update(agents, active_size):
    temp = np.zeros(active_size, dtype=np.int32)
    for i in nb.prange(active_size):
        if agents[i, 2] > 2:
            temp[i] = 10

    agents[:active_size, 0] += temp
    return agents
