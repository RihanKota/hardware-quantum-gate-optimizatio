import numpy as np
import matplotlib.pyplot as plt

from src.pulses.pulse_utils import save_plot



def gaussian_pulse(
        amplitude=1.0,
        duration=100,
        sigma=20
):

    """
    Generates Gaussian pulse

    Parameters:
        amplitude : pulse strength
        duration  : pulse length (ns)
        sigma     : width

    Returns:
        pulse waveform
    """

    t = np.arange(duration)


    pulse = amplitude * np.exp(
        -((t-duration/2)**2)
        /
        (2*sigma**2)
    )


    return t, pulse



if __name__ == "__main__":


    time, pulse = gaussian_pulse()


    plt.plot(
        time,
        pulse,
        linewidth=2
    )


    save_plot(
        "gaussian_pulse.png",
        "Gaussian Pulse"
    )
