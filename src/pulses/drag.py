import numpy as np

<<<<<<< HEAD

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
=======
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
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13


    pulse = (
        gaussian
        +
<<<<<<< HEAD
        1j*beta*derivative
    )


    return pulse
=======
        1j * beta * derivative
    )

    


    return t,pulse
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13
