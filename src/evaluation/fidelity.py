import numpy as np


def state_fidelity(final_state, target_state):

    final_state = final_state / np.linalg.norm(final_state)

    target_state = target_state / np.linalg.norm(target_state)

    overlap = np.vdot(
        target_state,
        final_state
    )

    return np.abs(overlap)**2



def x_gate_target():

    # Ideal X gate output
    # |0> -> |1>

    return np.array(
        [
            0,
            1,
            0
        ],
        dtype=complex
    )
