"""
Part 1: Computational Script (Fluid-Structure Force Visualization)This Python script models an advanced engineering scenario: a fluid flowing over a structural beam. It solves the Navier-Stokes/Advection-Diffusion simplification for fluid velocity, calculates the resulting dynamic fluid pressure field, and maps that pressure as a structural bending force along a cantilever beam using the Euler-Bernoulli beam theory.
"""
# pip install numpy scipy matplotlib


import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

# =====================================================================
# 1. PARAMETERS & CONFIGURATION
# =====================================================================
# Domain configuration
L_fluid = 10.0      # Length of fluid domain (m)
L_beam = 4.0        # Length of structural beam (m)
Nx_fluid = 100      # Fluid spatial grid points
Nx_beam = 50        # Structural spatial grid points

# Physical properties
rho_fluid = 1.225   # Fluid density (kg/m^3)
U_infinity = 25.0   # Freestream incoming fluid velocity (m/s)
viscosity = 1.8e-5  # Dynamic viscosity of fluid (Pa*s)
E = 2.0e11          # Young's Modulus of structural beam (Steel: 200 GPa)
I = 8.33e-6         # Area Moment of Inertia of the beam cross-section (m^4)

# Grid generation
x_fluid = np.linspace(0, L_fluid, Nx_fluid)
x_beam = np.linspace(0, L_beam, Nx_beam)
dx_fluid = L_fluid / (Nx_fluid - 1)
dx_beam = L_beam / (Nx_beam - 1)

# =====================================================================
# 2. NUMERICAL MODELING: FLUID DOMAIN (FVM/FDM Approximation)
# =====================================================================
# Initialize fluid velocity field (U) across the spatial grid
U_fluid = np.ones(Nx_fluid) * U_infinity

# Solve steady-state velocity profile with boundary layers using a relaxation scheme
# Boundary Conditions: U(0) = U_infinity (Inlet), U(Wall/Beam Boundary) = 0 (No-Slip)
for iteration in range(500):
    U_old = U_fluid.copy()
    for i in range(1, Nx_fluid - 1):
        # Central difference approximation for fluid momentum diffusion
        diffusion = viscosity * (U_old[i+1] - 2*U_old[i] + U_old[i-1]) / (dx_fluid**2)
        # Upwind difference approximation for fluid momentum advection
        advection = U_old[i] * (U_old[i] - U_old[i-1]) / dx_fluid
        # Update field with a relaxation step
        U_fluid[i] = U_old[i] + 0.01 * (diffusion - advection)

# Compute fluid Dynamic Pressure field (Bernoulli Principle: P = 0.5 * rho * U^2)
pressure_fluid = 0.5 * rho_fluid * (U_infinity**2 - U_fluid**2)

# Interp fluid pressures onto structural beam nodes (Data Exchange Boundary)
distributed_load = np.interp(x_beam, x_fluid, pressure_fluid)

# =====================================================================
# 3. NUMERICAL MODELING: STRUCTURAL DOMAIN (FEM/Finite Difference)
# =====================================================================
# Solve Euler-Bernoulli Beam Bending Equation: E*I*(d^4_w / dx^4) = q(x)
# Constructing a pentadiagonal stiffness matrix (A) for the system
A_matrix = np.zeros((5, Nx_beam)) # Banded format for optimized scipy solver

# Populate pentadiagonal bands based on central difference coefficients
A_matrix[0, 2:] = 1.0       # Upper 2nd diagonal
A_matrix[1, 1:] = -4.0      # Upper 1st diagonal
A_matrix[2, :] = 6.0        # Central diagonal
A_matrix[3, :-1] = -4.0     # Lower 1st diagonal
A_matrix[4, :-2] = 1.0      # Lower 2nd diagonal

# Enforce Boundary Conditions for a Cantilever Beam (Fixed at x=0, Free at x=L)
# Fixed Base (w=0, dw/dx=0 at i=0)
A_matrix[:, 0] = 0.0; A_matrix[2, 0] = 1.0  # Displacement zero
A_matrix[:, 1] = 0.0; A_matrix[2, 1] = 1.0  # Slope zero approximation

# Free Tip Boundary Conditions (d^2_w/dx^2 = 0, d^3_w/dx^3 = 0 at i=N-1)
A_matrix[:, -2] = 0.0; A_matrix[2, -2] = 1.0
A_matrix[:, -1] = 0.0; A_matrix[2, -1] = 1.0

# Prepare force load vector scale factor
load_factor = (dx_beam**4) / (E * I)
B_vector = distributed_load * load_factor
B_vector[0] = 0.0
B_vector[1] = 0.0
B_vector[-2] = 0.0
B_vector[-1] = 0.0

# Execute high-performance banded solver (Computational Modeling phase)
beam_deflection = solve_banded((2, 2), A_matrix, B_vector)

# =====================================================================
# 4. DATA VISUALIZATION AND PLOTTING
# =====================================================================
fig, axes = plt.subplots(3, 1, figsize=(10, 12))

# Subplot 1: Fluid Velocity Profile
axes[0].plot(x_fluid, U_fluid, color='blue', lw=2)
axes[0].set_title("Fluid Velocity Profile over Boundary Grid", fontsize=12, fontweight='bold')
axes[0].set_xlabel("Fluid Domain Length (meters)")
axes[0].set_ylabel("Velocity (m/s)")
axes[0].grid(True, linestyle='--')

# Subplot 2: Dynamic Pressure Transferred to Structural Surface
axes[1].plot(x_beam, distributed_load, color='orange', lw=2, linestyle='--')
axes[1].fill_between(x_beam, distributed_load, color='orange', alpha=0.1)
axes[1].set_title("Calculated Fluid Pressure Force on Beam Structure ($q(x)$)", fontsize=12, fontweight='bold')
axes[1].set_xlabel("Beam Length axis (meters)")
axes[1].set_ylabel("Force Load (N/m)")
axes[1].grid(True, linestyle='--')

# Subplot 3: Structural Elastic Beam Deflection Curve
axes[2].plot(x_beam, beam_deflection * 1e3, color='red', lw=2.5)
axes[2].set_title("Resulting Structural Beam Elastic Deflection", fontsize=12, fontweight='bold')
axes[2].set_xlabel("Beam Length axis (meters)")
axes[2].set_ylabel("Deflection (millimeters)")
axes[2].grid(True, linestyle='--')

plt.tight_layout()
plt.show()
