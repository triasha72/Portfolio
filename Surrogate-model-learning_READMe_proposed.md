# Surrogate Model Learning

A hands-on study of surrogate modeling for expensive engineering and scientific simulations. The repository focuses on Gaussian Processes, response-surface methods, radial-basis functions, uncertainty behavior, and the effect of sampling and feature representation on approximation quality.

## Current experiments

### 1. GP surrogate for the Branin function
- 20 Latin-hypercube training samples
- **R² = 0.9553**
- uncertainty increases in weakly sampled regions

### 2. Cantilever-beam deflection surrogate
- initial 30-sample experiment: R² = 0.64
- final 80-sample experiment with log-scaled inputs
- **R² = 1.0 · MAPE = 0.26%**

### 3. Surrogate-method comparison
| Method | R² | MAPE | Train time |
|---|---:|---:|---:|
| RSM | 0.247 | 1763% | 0.004 s |
| GP | 1.000 | 0.55% | 0.146 s |
| RBF | 0.895 | 187% | 0.002 s |

The comparison is a controlled learning experiment, not a universal ranking of surrogate methods.

## Tools
Python · NumPy · SciPy · scikit-learn · pyDOE2 · Matplotlib · Jupyter

## Run
```bash
pip install -r Requirements.txt
jupyter notebook
```

## Current scope
This repository currently contains the three notebook studies above. Future multifidelity or neural-operator work should be added only when it has a reproducible implementation and evidence in this repository.
