import numpy as np


def drag_pulse(
        sigma=20,
        beta=0.5,
        duration=100
):

    t=np.arange(duration)

    center=duration/2


    gaussian=np.exp(
        -(t-center)**2 /
        (2*sigma**2)
    )


    derivative=-(t-center)/(sigma**2)*gaussian


    pulse = (
        gaussian
        +
        1j*beta*derivative
    )


    return pulse