import matplotlib

# Use GUI backend for showing plots
matplotlib.use("QtAgg")

import matplotlib.pyplot as plt
import os


def plot_comparison():

    # Create results folder if it does not exist
    os.makedirs(
        "results",
        exist_ok=True
    )

    methods = [
        "Gaussian Pulse",
        "Optimized DRAG"
    ]

    # Replace these values with your actual results
    fidelity = [
        0.732842,       # Gaussian result
        0.999791       # DRAG optimized result
    ]

    leakage = [
        0.034626,       # Gaussian leakage
        0.009706        # DRAG optimized leakage
    ]


    fig, ax = plt.subplots(
        1,
        2,
        figsize=(10,4)
    )


    # Fidelity plot
    ax[0].bar(
        methods,
        fidelity,
        color=[
            "blue",
            "green"
        ]
    )

    ax[0].set_title(
        "Gate Fidelity Comparison"
    )

    ax[0].set_ylabel(
        "Fidelity"
    )

    ax[0].set_ylim(
        0,
        1
    )


    # Leakage plot
    ax[1].bar(
        methods,
        leakage,
        color=[
            "red",
            "orange"
        ]
    )

    ax[1].set_title(
        "Leakage Comparison"
    )

    ax[1].set_ylabel(
        "Leakage"
    )


    plt.tight_layout()


    # Save figure
    plt.savefig(
        "results/comparison.png",
        dpi=300
    )


    print(
        "Saved: results/comparison.png"
    )


    plt.show()



if __name__ == "__main__":

    plot_comparison()