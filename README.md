# SAT-Solver
This project is a Python implementation of a SAT-solver, which determines the satisfiability of CNF (Conjunctive Normal Form) files using two algorithms: the DPLL algorithm and a naive algorithm.

## Overview
The SAT-solver accepts a path to a CNF file as an argument and runs both the DPLL and naive algorithms to determine if the CNF is satisfiable (SAT) or unsatisfiable (UNSAT). Additionally, the solver measures and displays the execution time for each algorithm. The DPLL algorithm is a heuristic algorithm and consistently runs faster than the naive algorithm. In the case of a satisfiable result (SAT), the solver also returns which variables receive true and which receive false for both algorithms.

## Features
- Two Algorithms: Implements both the DPLL and naive algorithms to solve SAT problems.
- Performance Comparison: Measures and displays the runtime of each algorithm.
- Accurate Results: Both algorithms provide the same satisfiability result for the CNF file.
- Variable Assignment: Returns the variable assignments (true/false) in case of a satisfiable result.

## Installation
To build and run the code, follow these steps:

Clone the repository:
```bash
git clone https://github.com/yourusername/sat-solver.git
cd sat-solver
```
Run the SAT-solver:
```bash
python sat_solver.py /path/to/cnf_file.cnf
```

### Example CNF File
An example CNF file is provided in the repository to help you get started. The format of the CNF file should be compatible with standard DIMACS CNF format.

### Running example
![sat](https://github.com/tomerp1812/SAT-Solver/assets/110912180/754abe51-8513-4d32-9b8e-90c88611eeaf)
