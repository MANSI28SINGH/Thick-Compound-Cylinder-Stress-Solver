# Thick and Compound Cylinder Stress Distribution Solver (GUI)

An interactive Python application developed to calculate, analyze, and visualize the structural stress distribution across the walls of thick-walled and compound cylinders. By executing numerical evaluations of classical **Lame's Equations**, the software maps the precise variations of **Hoop Stress ($\sigma_\theta$)** and **Radial Stress ($\sigma_r$)** under internal, external, and interface shrink-fit pressures.

---

## Technical Context & Core Engineering Mechanics

In pressure vessel design, thin-walled assumptions fail when the wall thickness exceeds approximately 10% of the inner radius. Instead, variations in stress fields across the radial continuum must be treated via continuum mechanics frameworks.

This program models two primary physical pressure vessel setups:

### 1. Monobloc Thick Cylinders
Solves Lame's structural mechanics constants ($A$ and $B$) under specific boundary constraints to map parabolic radial decay curves:

$$\sigma_\theta = A + \frac{B}{r^2} \quad (\text{Hoop/Circumferential Stress})$$

$$\sigma_r = A - \frac{B}{r^2} \quad (\text{Radial Stress})$$

### 2. Shrink-Fit Compound Cylinders
Models a multi-layered cylinder system where an outer jacket is heated and shrunk onto an inner sleeve. This induces initial compressive residual stresses at the common mating radius ($r_c$), lowering the peak tensile hoop stresses experienced under eventual internal operating pressures.

The solver applies strict **superposition mechanics** to calculate separate matrix operations across both internal ($r_i \le r \le r_c$) and external ($r_c \le r \le r_o$) bounds.

---

## Application Capabilities & Software Stack

* **Interactive Menu Framework:** Drives a main routing window enabling designers to transition instantly between standalone Thick-Walled configurations and Compound multi-layer frameworks.
* **Discrete Numerical Continuum:** Leverages `NumPy` vector grids (`np.linspace`) to calculate exact localized continuum stress tensors across 1,000 internal steps.
* **Auto-Annotating Visualizer:** Leverages `Matplotlib` engines to map continuous stress curves, automatically calculating and dynamically placing digital text banners marking peak global extremes.

---

## How to Execute the Tool

### Required Environment Dependencies
Ensure your Python ecosystem contains `numpy` and `matplotlib`:
```bash
pip install numpy matplotlib
