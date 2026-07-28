from src.pulses.drag import drag_pulse
from src.simulation.qubit_model import TransmonQubit
from src.evaluation.fidelity import (
    state_fidelity,
    x_gate_target
)


_, pulse = drag_pulse(
    sigma=20,
    beta=0.5
)


qubit = TransmonQubit()


state = qubit.evolve(
    pulse
)


print(state)

print(
    "Fidelity:",
    state_fidelity(
        state,
        x_gate_target()
    )
)