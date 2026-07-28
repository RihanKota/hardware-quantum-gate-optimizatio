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


    from scipy.optimize import minimize


    result = minimize(
        cost_function,
        x0=[20,0.5],
        method="L-BFGS-B",
        bounds=[
            (5,40),       # sigma
            (-1,1)        # beta
        ]
    )

    print("\nOptimization Result")
    print(result.x)
