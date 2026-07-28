import json
import os

from scipy.optimize import minimize

from src.pulses.drag import drag_pulse

from src.simulation.qubit_model import TransmonQubit

from src.evaluation.fidelity import calculate_fidelity

from src.evaluation.leakage import calculate_leakage

from src.evaluation.results import save_result, plot_result



# Create qubit model
qubit = TransmonQubit()


# Store optimization history
history = []



def evaluate_parameters(parameters):
    """
    Generate pulse, simulate qubit evolution,
    calculate fidelity and leakage.
    """

    amplitude, duration = parameters


    pulse = drag_pulse(
        amplitude,
        duration
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
    Evaluate final optimized pulse.
    """

    return evaluate_parameters(
        (
            amplitude,
            duration
        )
    )




def cost(parameters):
    """
    Optimization cost function.

    Lower cost is better.

    Objective:
        maximize fidelity
        minimize leakage
    """

    amplitude, duration = parameters


    fidelity, leakage = evaluate_parameters(
        (
            amplitude,
            duration
        )
    )


    # Leakage penalty
    leakage_weight = 5.0


    cost_value = (
        1 - fidelity
        +
        leakage_weight * leakage
    )


    history.append(
        {
            "amplitude": amplitude,
            "duration": duration,
            "fidelity": fidelity,
            "leakage": leakage,
            "cost": cost_value
        }
    )


    print(
        amplitude,
        duration,
        fidelity,
        leakage
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
            "maxiter": 1000,
            "xatol": 1e-8,
            "fatol": 1e-8
        }
    )



    # Best optimized parameters

    best_amplitude = result.x[0]

    best_duration = result.x[1]



    # Evaluate optimized pulse

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



    # Save normal result file

    save_result(
        best_amplitude,
        best_duration,
        best_fidelity,
        best_leakage
    )



    # Create results folder

    os.makedirs(
        "results",
        exist_ok=True
    )



    # Save JSON for README update

    result_data = {

        "amplitude":
            float(best_amplitude),

        "duration":
            float(best_duration),

        "fidelity":
            float(best_fidelity),

        "leakage":
            float(best_leakage)

    }



    with open(
        "results/latest_result.json",
        "w"
    ) as file:


        json.dump(
            result_data,
            file,
            indent=4
        )



    print(
        "\nSaved latest_result.json:"
    )


    print(
        result_data
    )



    # Update README automatically

    os.system(
        "python update_readme.py"
    )



    # Save optimization graph

    plot_result(
        history
    )


    print(
        "\nOptimization completed."
    )