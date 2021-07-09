from __future__ import print_function
from simtk.openmm.app import *
from simtk.openmm import * 
import simtk.openmm as mm
from simtk.unit import *
from simtk import unit
from sys import stdout
import mdtraj as md
import numpy as np


input_pdb = '/home/marpoli/snic2020-6-15/Marco/1_Virtual_Cell_Model/Plectasin/MD/1ZFU_box.pdb'
workdir =  '/home/marpoli/snic2020-6-15/Marco/1_Virtual_Cell_Model/Plectasine/MD/'                
                
### Input ###
pdb = PDBFile(input_pdb) # For simulation
file = md.load(input_pdb)# To select atoms

### Force Field and Water Model ###
forcefield = ForceField('/Users/michael/Desktop/VCM_repo/Molecular_dynamics/amber99sb_Cl.xml', 'spce.xml')

###Modeller object###  replace "pdb" with "modeller" in system, simulation and simulation.context
modeller = Modeller(pdb.topology, pdb.positions)

### Protein protonation state according to the selected pH ###
modeller.addHydrogens(forcefield, pH=2) 

### Fill the box with water molecules, and neutralize it ### 
modeller.addSolvent(forcefield,  neutralize=True, negativeIon='Cl-')

### Create system
system = forcefield.createSystem(modeller.topology, 
                                 nonbondedMethod=PME, 
                                 nonbondedCutoff=1.0*unit.nanometers, 
                                 constraints=HBonds, 
                                 ewaldErrorTolerance=0.0005, 
                                 removeCMMotion=True)
                                 
    
### Fixing the backbone positions ###
backbone = file.topology.select('backbone')
backbone_list = []
for i in backbone:
    backbone_list.append(i)
for a in backbone_list:
    system.setParticleMass(int(a), 1e10)

### Integrator ###
integrator = mm.LangevinIntegrator(298.15*kelvin, 1.0/unit.picoseconds, 4.0*unit.femtoseconds)
integrator.setConstraintTolerance(0.00001)

### Platform ###
platform = mm.Platform.getPlatformByName('CUDA')
properties = {'CudaPrecision': 'mixed', 'CudaDeviceIndex': '0,1'}

### Start Simulation ###
simulation = Simulation(modeller.topology, system, integrator, platform, properties)
simulation.context.setPositions(modeller.positions)

### Minimization energy ###
print('Minimizing...')
simulation.minimizeEnergy()
print('Done!')

### Save file ###
positions = simulation.context.getState(getPositions=True, enforcePeriodicBox=False).getPositions()
PDBFile.writeFile(simulation.topology, positions, open('min.pdb', 'w'), keepIds=True)


                