[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mlund/SI-virtual-cell-model/HEAD)

# Electronic Notebook: Virtual Cell Model for Osmotic Pressure Calculation of Charged Biomolecules

This is an electronic notebook for reproducing the simulations and related analysis
for the scientific paper titled above.

## Directory layout

- `Monte_Carlo/` Coarse grained one-body and two-body Metropolic Monte Carlo simulations
- `Monlecular_Dynamics/` Atomistic one-body molecular dynamics simulations with virtual ion-boundary

## Requirements

To run the Notebooks online, click on the _Launch Binder_ logo above. Alternatively, if you want to run on your own computer,
install python using e.g. [Miniconda](https://conda.io/miniconda.html) or [Anaconda](https://docs.conda.io))
and make sure all required packages are loaded by issuing the following terminal commands

``` bash
    conda env create -f environment.yml
    source activate virtualcell
    jupyter-notebook
```
