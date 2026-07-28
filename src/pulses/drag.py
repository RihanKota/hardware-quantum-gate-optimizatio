import numpy as np

def drag_pulse(
        sigma=20,
        beta=0.5,
        amplitude=2.0,
        duration=100
):

    t = np.arange(duration)

    gaussian = np.exp(
        -0.5*((t-duration/2)/sigma)**2
    )

    gaussian = (
        amplitude *
        gaussian /
        np.max(gaussian)
    )


    derivative = np.gradient(gaussian)


    pulse = (
        gaussian
        +
        1j * beta * derivative
    )

    


    return t,pulse
