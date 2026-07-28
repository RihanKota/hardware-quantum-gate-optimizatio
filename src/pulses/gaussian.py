import numpy as np


def gaussian_pulse(
        sigma=20,
        duration=100
):

    t = np.arange(duration)

    pulse = np.exp(
        -(t-duration/2)**2 /
        (2*sigma**2)
    )

    return pulse