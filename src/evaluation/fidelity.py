import numpy as np


<<<<<<< HEAD
def calculate_fidelity(
        state
):

    target=np.array(
=======
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
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13
        [
            0,
            1,
            0
        ],
        dtype=complex
<<<<<<< HEAD
    )


    fidelity=abs(
        np.vdot(
            target,
            state
        )
    )**2


    return fidelity
=======
    )
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13
