# TecX_Multiphysics-HPC-Solvers-Masterclass

## TecX Multiphysics HPC Solvers Masterclass

```
TecX_Multiphysics-HPC-Solvers-Masterclass/
│
├── .github/
│   └── workflows/
│       └── cpp-ci.yml             # Automated compiler checks for your solver engines
│
├── 01_theory_and_calculus/
│   ├── README.md                  # Comprehensive continuum mechanics & mathematical foundations
│   └── governing_equations.tex    # LaTeX source code for all PDE derivations
│
├── 02_numerical_discretization/
│   ├── README.md                  # Detailed curriculum for FDM, FEM, FVM, and PLIC
│   └── 1d_heat_fdm_solver.py      # Basic foundational script (1D transient heat mesh)
│
├── 03_computational_multiphysics/
│   ├── README.md                  # Detailed guide on FSI, ALE, and Reactive Fluids
│   ├── transient_fsi_vibration.py # Full 2D Transient FSI with Active Vibration Control
│   └── high_speed_multiphysics.py # Compressible Gas Shock hitting Multiphase Liquid Front
│
├── 04_reactive_and_phase_change/
│   ├── README.md                  # Thermal Phase-Change (Boiling) & Arrhenius Combustion theory
│   └── reactive_boiling_engine.py # Combined Multiphase VOF, Lee Boiling, and Arrhenius Reaction
│
├── 05_high_performance_computing/
│   ├── README.md                  # Sparse matrices, Kronecker products, MPI, and GPU optimization
│   ├── parallel_matrix_core.py    # 2D Implicit Crank-Nicolson Solver using Sparse CSR Matrices
│   ├── parallel_cg.cpp            # 5-Million Element Symmetric CG Solver (C++ / OpenMP)
│   └── gpu_cg_core.py             # 8-Million Element Asymmetric Krylov Solver (Python / PyCUDA)
│
├── LICENSE                        # MIT or Apache 2.0 open-source software license
└── README.md                      # The Master Repository landing page and learning curriculum

```
# High-Performance Multiphysics Solvers & Computational Foundations

Welcome to the definitive repository for advanced continuous mechanics modeling, numerical discretization schemes, and parallelized Krylov subspace solvers. This repository tracks the full evolutionary lifecycle of advanced scientific engineering simulations: transitioning from pencil-and-paper continuous calculus, through numerical discretization matrices, up to distributed-memory high-performance computing (HPC) clusters.

## 🚀 Repository Capabilities Architecture
* **Continuum Mechanics Engines**: Implementations mapping multi-phase Navier-Stokes equations, compressible Euler vectors, and structural elastodynamics equations.
* **Transient Multi-Physics Fields**: 2D/3D matrix assembly methods for Fluid-Structure Interaction (FSI), active vibration damping controllers, and Arbitrary Lagrangian-Eulerian (ALE) grid warping arrays.
* **Advanced Non-Linear Closures**: High-fidelity modules modeling 5th-Order WENO shock-capturing, PLIC geometric boundary reconstructions, thermal Lee boiling dynamics, and Arrhenius combustion kinetics.
* **Massively Parallel Solvers**: Compile-ready distributed computing frameworks writing multi-core C++ (via OpenMP) and parallelized GPU device kernels (via PyCUDA).

---

## 📂 Core Folder Guide & Learning Path

### [01. Theory & Calculus](./01_theory_and_calculus/)
* **Foundations**: Derivation of the Material Derivative operator connecting Lagrangian particle arrays to fixed Eulerian calculation windows:
  $$\frac{D\phi}{Dt} = \frac{\partial \phi}{\partial t} + (\mathbf{v} \cdot \nabla)\phi$$
* **PDE Compilations**: Complete mathematical breakdowns of the Cauchy stress tensor, linear Hookean strains, and multi-dimensional continuum mechanics laws.

### [02. Numerical Discretization](./02_numerical_discretization/)
* **Approximations**: Transformation of raw calculus partial derivatives into discrete algebraic grid operations using Taylor Series configurations.
* **Domain Mappings**: Deep-dives into the Finite Element Method (FEM) weak-form formulations for structural mechanics and the Finite Volume Method (FVM) conservation flux arrays for fluid layers.

### [03. Computational Multiphysics](./03_computational_multiphysics/)
* **Aeroelastic Resonances**: Explicit code solving second-order hyperbolic structural dynamics systems using unconditionally stable, implicit Newmark-$\beta$ integration time matrices.
* **Shock-Capturing Fluidics**: Upwind Riemann Solver integrations designed to track sharp supersonic flow changes without causing computational divergence or numerical oscillations.

### [04. Reactive & Phase-Change Models](./04_reactive_and_phase_change/)
* **Phase Interfaces**: Phase distribution boundaries managed with volume indicator variables ($\alpha$). Geometric boundaries are kept perfectly sharp using Piecewise Linear Interface Calculation (PLIC) normal updates.
* **Energetic Closures**: Multiphysics codes coupling the mass-transfer properties of the Lee vaporization model alongside the exothermic heat releases of Arrhenius species combustion kinetics.

### [05. High-Performance Computing (HPC)](./05_high_performance_computing/)
* **Matrix Architectures**: Code scaling multidimensional calculations into flattened 1D arrays through Kronecker Tensor Products ($\otimes$), creating sparse pentadiagonal/septadiagonal systems.
* **Distributed Clusters**: Documentation detailing distributed-memory load handling using MPI Halo Exchanges and non-blocking boundaries.
* **Krylov Solvers**: Custom parallelized algorithmic loops breaking open the operational black boxes of the **Conjugate Gradient (CG)** and **GMRES** sparse matrix iterative matrix solvers.

---

## 🛠️ Execution & Environment Controls

### Running the Multi-Core CPU C++ Solvers
To compile and execute the parallelized 5-million element Conjugate Gradient engine on any multi-core modern CPU architecture:
```bash
g++ -O3 -fopenmp ./05_high_performance_computing/parallel_cg.cpp -o parallel_cg
./parallel_cg
```

### Running the Python GPU Acceleration Engines
To stream matrix arrays across the PCIe hardware bus and launch the 8-million variable solver block kernels using parallelized GPU cores:
```bash
pip install numpy scipy matplotlib pycuda
python ./05_high_performance_computing/gpu_cg_core.py
```

---

## 📜 Academic Reference Literature
1. *An Introduction to Computational Fluid Dynamics: The Finite Volume Method* — H. Versteeg & W. Malalasekera.
2. *The Finite Element Method for Solid and Structural Mechanics* — O.C. Zienkiewicz & R.L. Taylor.
3. *Iterative Methods for Sparse Linear Systems* — Y. Saad (The foundational handbook for Krylov subspace, CG, and GMRES mechanics).

## 🪪 License
Distributed under the open-source MIT Software License. Review the root `LICENSE` file for detailed developer rights mappings.
