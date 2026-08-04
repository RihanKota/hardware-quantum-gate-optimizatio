# Hardware Quantum Gate Optimization

## Executive Summary
**Mitigating Leakage in Transmon Qubits via DRAG Pulse Optimization.**

In quantum computing hardware, specifically superconducting Transmon qubits, pulse shaping is critical to maximizing gate fidelity. The primary challenge in fast qubit control is **leakage**—the unwanted excitation of the qubit from the computational subspace ($|0\rangle$, $|1\rangle$) into higher, non-computational energy states (such as $|2\rangle$). 

This project demonstrates the optimization of quantum gates by comparing standard Gaussian microwave pulses against **DRAG (Derivative Removal by Adiabatic Gate)** pulses. By utilizing analytical pulse shaping, we can significantly suppress leakage and improve state fidelity, allowing for faster and more reliable quantum operations.

## Theory & Methodology

### The Leakage Problem
Transmons are weakly anharmonic oscillators. Because the energy difference between the $|1\rangle \rightarrow |2\rangle$ transition is very close to the $|0\rangle \rightarrow |1\rangle$ transition, driving a fast Gaussian pulse can accidentally populate the $|2\rangle$ state. 

### DRAG Optimization
The DRAG technique corrects this by adding a derivative component to the out-of-phase ($Q$) quadrature of the control pulse. This tailored spectral profile minimizes the Fourier components at the $|1\rangle \rightarrow |2\rangle$ transition frequency, effectively preventing leakage while maintaining rapid gate times.

## Project Architecture

The optimization workflow is:
             Pulse Parameters
                   |
                   v
          DRAG Pulse Generator
                   |
                   v
          Transmon Qubit Model
                   |
                   v
          Quantum State Evolution
                   |
                   v
    +--------------+--------------+
    |                             |
    v                             v
    Gate Fidelity Leakage Calculation
| |
+-------------+---------------+
|
v
Optimization Algorithm
|
v
Optimized Pulse Parameters
|
v
Results + Visualization

## Features

### 1. DRAG Pulse Optimization
The project uses Derivative Removal by Adiabatic Gate (DRAG) pulse shaping to reduce unwanted transitions between quantum energy levels.
Optimized parameters:
- Pulse amplitude
- Pulse duration
- Pulse shape parameters

### 2. Transmon Qubit Simulation
A simplified transmon qubit model is used to simulate quantum state evolution under applied control pulses.
The simulation evaluates:
- Final quantum state
- Population transfer
- Leakage to higher energy states

### 3. Fidelity Optimization
The optimizer maximizes the gate fidelity:
\[
F = |\langle \psi_{target}|\psi_{final}\rangle|^2
\]
Higher fidelity indicates better quantum gate performance.

### 4. Leakage Reduction
Leakage measures unwanted population outside the computational subspace.
The optimization objective is:
\[
Cost = (1-Fidelity)+Leakage
\]
The optimizer searches for parameters with:
- Maximum fidelity
- Minimum leakage

## Code & Reproducibility

This repository contains the simulation environment and pulse optimization scripts to reproduce these findings.

### Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/hardware-quantum-gate-optimization.git
```

### Running the Optimization
*(Ensure your virtual environment is active and dependencies from `requirements.txt` are installed.)*

1. **Run the Pulse Simulation**: Execute the testing script to simulate the DRAG pulse and calculate fidelity/leakage.
   ```bash
   python test_pulse.py
   ```
2. **Generate Visualizations**: Run the comparison script to generate fidelity and leakage charts.
   ```bash
   python comparison.py
   ```
3. **Update Results**: Automate the logging of your latest optimization metrics.
   ```bash
   python update_readme.py
   ```

---

<!-- OPTIMIZATION_RESULTS_START -->

## Latest Optimization Result

| Parameter | Value |
|---|---|
| Amplitude | 21.747534 |
| Duration | 0.484300 |
| Fidelity | 0.9988681474 |
| Leakage | 0.0018303995 |

Last Updated:

2026-07-28 11:57:25

<!-- OPTIMIZATION_RESULTS_END -->
