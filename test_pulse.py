from src.pulses.drag import drag_pulse
from src.simulation.qubit_model import TransmonQubit
<<<<<<< HEAD

from src.evaluation.fidelity import calculate_fidelity
from src.evaluation.leakage import calculate_leakage

from src.evaluation.results import save_result


pulse = drag_pulse(
=======
from src.evaluation.fidelity import (
    state_fidelity,
    x_gate_target
)


_, pulse = drag_pulse(
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13
    sigma=20,
    beta=0.5
)


qubit = TransmonQubit()


state = qubit.evolve(
    pulse
)


<<<<<<< HEAD
print("State simulation completed")


fidelity = calculate_fidelity(
    state
)


leakage = calculate_leakage(
    state
)


print(
    "Fidelity:",
    fidelity
)


print(
    "Leakage:",
    leakage
)


save_result(
    "DRAG",
    fidelity,
    leakage
=======
print(state)

print(
    "Fidelity:",
    state_fidelity(
        state,
        x_gate_target()
    )
>>>>>>> 611e7cc82fd5e6dda4b77c9ea91044fb78fe8b13
)