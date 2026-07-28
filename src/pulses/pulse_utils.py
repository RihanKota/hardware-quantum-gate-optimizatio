import matplotlib.pyplot as plt
import os


def save_plot(filename, title):
    """
    Save pulse visualization to results/plots
    """

    os.makedirs(
        "results/plots",
        exist_ok=True
    )

    plt.title(title)
    plt.xlabel("Time (ns)")
    plt.ylabel("Amplitude")

    plt.grid(True)

    path = f"results/plots/{filename}"

    plt.savefig(
        path,
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    print(f"Saved: {path}")