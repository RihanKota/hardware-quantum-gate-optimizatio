import matplotlib.pyplot as plt
import os


def plot_pulse(
        pulse
):

    os.makedirs(
        "results",
        exist_ok=True
    )


    plt.plot(
        pulse.real,
        label="I"
    )


    plt.plot(
        pulse.imag,
        label="Q"
    )


    plt.legend()

    plt.title(
        "Optimized DRAG Pulse"
    )


    plt.savefig(
        "results/optimized_pulse.png"
    )


    plt.close()