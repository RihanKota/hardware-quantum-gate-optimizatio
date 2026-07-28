# Hardware Quantum Gate Optimization

## Overview

This project focuses on optimizing quantum control pulses for hardware-efficient quantum gates using numerical optimization techniques.

The main goal is to design high-quality control pulses for a transmon qubit by maximizing gate fidelity while reducing leakage errors.

The project implements:

- DRAG pulse generation
- Transmon qubit simulation
- Gate fidelity evaluation
- Leakage calculation
- Numerical pulse optimization
- Automatic result saving
- Performance visualization
- Automatic README result updating

---

# Project Architecture

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


---

# Features

## 1. DRAG Pulse Optimization

The project uses Derivative Removal by Adiabatic Gate (DRAG) pulse shaping to reduce unwanted transitions between quantum energy levels.

Optimized parameters:

- Pulse amplitude
- Pulse duration
- Pulse shape parameters

---

## 2. Transmon Qubit Simulation

A simplified transmon qubit model is used to simulate quantum state evolution under applied control pulses.

The simulation evaluates:

- Final quantum state
- Population transfer
- Leakage to higher energy states

---

## 3. Fidelity Optimization

The optimizer maximizes the gate fidelity:

\[
F = |\langle \psi_{target}|\psi_{final}\rangle|^2
\]

Higher fidelity indicates better quantum gate performance.

---

## 4. Leakage Reduction

Leakage measures unwanted population outside the computational subspace.

The optimization objective is:

\[
Cost = (1-Fidelity)+Leakage
\]

The optimizer searches for parameters with:

- Maximum fidelity
- Minimum leakage

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/hardware-quantum-gate-optimization.git