from src.pulses.drag import drag_pulse

from src.simulation.qubit_model import TransmonQubit

from src.evaluation.fidelity import calculate_fidelity

from src.evaluation.leakage import calculate_leakage

from src.evaluation.results import save_result



pulse=drag_pulse(
    sigma=20,
    beta=0.5
)


qubit=TransmonQubit()


state=qubit.evolve(
    pulse
)


print(state)



fidelity=calculate_fidelity(
    state
)


leakage=calculate_leakage(
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
)