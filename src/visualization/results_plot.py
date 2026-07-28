import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("QtAgg")

import json
import os



def plot_comparison():

    os.makedirs(
        "results",
        exist_ok=True
    )


    # Gaussian pulse result
    gaussian_fidelity = 0.7328
    gaussian_leakage = 0.06



    # Load DRAG optimization result

    with open(
        "results/optimization_results.json",
        "r"
    ) as file:

        drag_result = json.load(file)



    drag_fidelity = drag_result["fidelity"]

    drag_leakage = drag_result["leakage"]



    methods = [
        "Gaussian",
        "DRAG"
    ]


    fidelity = [
        gaussian_fidelity,
        drag_fidelity
    ]


    leakage = [
        gaussian_leakage,
        drag_leakage
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
        "Gate Fidelity"
    )


    ax[0].set_ylim(
        0,
        1
    )


    ax[0].set_ylabel(
        "Fidelity"
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
        "Leakage"
    )


    ax[1].set_ylabel(
        "Leakage"
    )



    plt.suptitle(
        "Pulse Optimization Comparison"
    )


    plt.tight_layout()



    plt.savefig(
        "results/comparison.png",
        dpi=300
    )


    plt.close()



if __name__ == "__main__":

    plot_comparison()