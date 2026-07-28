import json
import os
import matplotlib.pyplot as plt


def save_result(amplitude, duration, fidelity, leakage):

    os.makedirs("results", exist_ok=True)

    data = {
        "amplitude": float(amplitude),
        "duration": float(duration),
        "fidelity": float(fidelity),
        "leakage": float(leakage)
    }

    with open(
        "results/optimization_results.json",
        "w"
    ) as f:
        json.dump(data, f, indent=4)


    print("\nSaved Result:")
    print(data)



def plot_result(history):

    os.makedirs("results", exist_ok=True)

    iterations = range(len(history))

    fidelity = [
        x["fidelity"]
        for x in history
    ]

    leakage = [
        x["leakage"]
        for x in history
    ]


    plt.figure(figsize=(8,5))

    plt.plot(
        iterations,
        fidelity,
        label="Fidelity"
    )

    plt.plot(
        iterations,
        leakage,
        label="Leakage"
    )

    plt.xlabel("Iteration")
    plt.ylabel("Value")

    plt.title(
        "Pulse Optimization Performance"
    )

    plt.legend()

    plt.grid()

    plt.savefig(
        "results/optimization_plot.png",
        dpi=300
    )

    plt.close()