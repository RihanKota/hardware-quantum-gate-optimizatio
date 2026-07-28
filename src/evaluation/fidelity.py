import numpy as np


def calculate_fidelity(
        state
):

    target=np.array(
        [
            0,
            1,
            0
        ],
        dtype=complex
    )


    fidelity=abs(
        np.vdot(
            target,
            state
        )
    )**2


    return fidelity