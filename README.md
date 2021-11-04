[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mlund/SI-virtual-cell-model/HEAD)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5645948.svg)](https://doi.org/10.5281/zenodo.5645947)

# Electronic Notebook: Virtual Cell Model for Osmotic Pressure Calculation of Charged Biomolecules

This Electronic Notebook can be used to reproduce the simulations and analysis presented in
the research paper [Virtual Cell Model for Osmotic Pressure Calculation of Charged Biomolecules](https://dx.doi.org/10.1063/5.0063717) published in _J. Chem. Phys._, 2021.

The osmotic pressure of dilute poly-electrolyte solutions containing charged macro-ions as well as counter-ions
can be computed directly from the particle distribution via the well-known _cell model_.
Originally derived within the Poisson-Boltzmann mean-field approximation, the cell model describes a poly-electrolyte
solution considering a single macro-ion centered into a cell, together with counter-ions needed to neutralize
the total cell charge.
While extensively applied in coarse-grained Monte Carlo (MC) simulations of continuum solvent systems, the cell
model neglects the macro-ion shape anisotropy and details of the surface charge distribution. By comparing one-body
and two-body coarse-grained Monte Carlo simulations we validate this approximation using a non-spherical macro-ion.
Next, we extend the cell model to all-atom molecular dynamics simulations and show that protein concentration-dependent osmotic pressures can be obtained by confining counter-ions in a virtual, spherical subspace defining the protein number density. Finally, we show the possibility of using specific interaction parameters for the protein-ion and ion-ion interactions, enabling studies of protein concentration-dependent ion-specific effects using merely a single protein molecule.

## Directory layout

- `Monte_Carlo/` Coarse grained one-body and two-body Metropolic Monte Carlo simulations
- `Monlecular_Dynamics/` Atomistic one-body molecular dynamics simulations with virtual ion-boundary

## Requirements

To run the Notebooks online, click on the _Launch Binder_ logo above. Alternatively, if you want to run on your own computer,
install python using e.g. [Miniconda](https://conda.io/miniconda.html) or [Anaconda](https://docs.conda.io)
and make sure all required packages are loaded by issuing the following terminal commands

``` bash
    conda env create -f environment.yml
    source activate virtualcell
    jupyter-notebook
```
