# TecX_Multiphysics-HPC-Solvers-Masterclass
TecX Multiphysics HPC Solvers Masterclass

```
Multiphysics-HPC-Solvers-Masterclass/
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
