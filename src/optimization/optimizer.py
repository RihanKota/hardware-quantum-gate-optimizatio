from scipy.optimize import minimize

from src.pulses.drag import drag_pulse

from src.simulation.qubit_model import TransmonQubit

from src.evaluation.fidelity import calculate_fidelity

from src.evaluation.leakage import calculate_leakage

from src.evaluation.results import save_result, plot_result


# Create qubit model
qubit = TransmonQubit()


# Store optimization history for plotting
history = []


def evaluate_parameters(parameters):
    """
    Generate pulse, simulate qubit evolution,
    and calculate fidelity/leakage.
    """

    sigma, beta = parameters


    pulse = drag_pulse(
        sigma,
        beta
    )


    state = qubit.evolve(
        pulse
    )


    fidelity = calculate_fidelity(
        state
    )


    leakage = calculate_leakage(
        state
    )


    return fidelity, leakage



def evaluate(amplitude, duration):
    """
    Wrapper function for testing final pulse.
    """

    return evaluate_parameters(
        (
            amplitude,
            duration
        )
    )



def cost(parameters):
    """
    Optimization objective.

    Lower cost is better.

    We maximize fidelity
    and minimize leakage.
    """

    sigma, beta = parameters


    fidelity, leakage = evaluate_parameters(
        (
            sigma,
            beta
        )
    )


    # Leakage penalty weight
    leakage_weight = 5.0


    cost_value = (
        1 - fidelity
        +
        leakage_weight * leakage
    )


    history.append(
        {
            "sigma": sigma,
            "beta": beta,
            "fidelity": fidelity,
            "leakage": leakage,
            "cost": cost_value
        }
    )


    return cost_value



if __name__ == "__main__":


    print("\nStarting optimization...")
    print("========================")


    initial_parameters = [
        20.0,
        0.5
    ]


    result = minimize(
        cost,
        initial_parameters,
        method="Nelder-Mead",
        options={
            "maxiter": 500,
            "xatol": 1e-8,
            "fatol": 1e-8
        }
    )



    # Best parameters found

    best_amplitude = result.x[0]

    best_duration = result.x[1]



    best_fidelity, best_leakage = evaluate(
        best_amplitude,
        best_duration
    )



    print("\nOptimization Result")
    print("===================")

    print(
        "Amplitude:",
        best_amplitude
    )

    print(
        "Duration:",
        best_duration
    )

    print(
        "Fidelity:",
        best_fidelity
    )

    print(
        "Leakage:",
        best_leakage
    )


    print(
        "\nOptimizer status:",
        result.message
    )



    # Save final result

    save_result(
        best_amplitude,
        best_duration,
        best_fidelity,
        best_leakage
    )



    # Save optimization graph

    plot_result(
        history
    )