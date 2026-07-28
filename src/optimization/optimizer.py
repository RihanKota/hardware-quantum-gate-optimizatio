import numpy as np

from scipy.optimize import minimize

from src.simulation.qubit_model import TransmonQubit

from src.evaluation.fidelity import (
    state_fidelity,
    x_gate_target
)

from src.evaluation.leakage import (
    leakage_probability
)

from src.pulses.drag import drag_pulse

qubit = TransmonQubit()



def cost_function(parameters):


    sigma, beta = parameters


    _, pulse = drag_pulse(
        sigma=sigma,
        beta=beta
    )


    final_state = qubit.evolve(
        np.real(pulse)
    )


    fidelity = state_fidelity(
        final_state,
        x_gate_target()
    )


    leakage = leakage_probability(
        final_state
    )


    cost = (
    1 - fidelity
    +
    10 * leakage
)

    
    print(
        f"""
    sigma  = {sigma:.3f}
    beta   = {beta:.3f}
    fidelity = {fidelity:.5f}
    leakage  = {leakage:.5f}
    cost     = {cost:.5f}
    """
    )

    return cost




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