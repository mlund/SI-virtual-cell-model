from __future__ import print_function
from simtk.openmm.app import *
from simtk.openmm import * 
import simtk.openmm as mm
from simtk.unit import *
from simtk import unit
from sys import stdout
import mdtraj as md
import numpy as np

workdir =  '/home/marpoli/snic2020-6-15/Marco/1_Virtual_Cell_Model/Plectasine/MD/' 
                
### Input ###
pdb = PDBFile('min.pdb') # For simulation
file = md.load('min.pdb') # To select atoms

### Force Field and Water Model ###
forcefield = ForceField('/Users/michael/Desktop/VCM_repo/Molecular_dynamics/amber99sb_F.xml', 'spce.xml')

###Modeller object###  replace "pdb" with "modeller" in system, simulation and simulation.context
modeller = Modeller(pdb.topology, pdb.positions)

### Protein protonation state according to the selected pH ###
modeller.addHydrogens(forcefield, pH=2) 

### Create system. Constraining the hbonds allowed for a larger integration time step, about 4/3 fs for Langevin dynamics but it crashed. So keep 2 fs
system = forcefield.createSystem(modeller.topology, 
                                 nonbondedMethod=PME, 
                                 nonbondedCutoff=1.0*unit.nanometers, 
                                 constraints=HBonds, 
                                 ewaldErrorTolerance=0.0005, 
                                 removeCMMotion=True)


protein_CI = file.topology.select('protein or name F') # Select protein and c.ions for reporters

### Add force to counterions ###
Cions = file.topology.select('name F')
force = CustomExternalForce('100*max(0, r-2.4)^2; r=sqrt((x-4.0)^2+(y-4.0)^2+(z-4.0)^2)')
system.addForce(force)
for i in Cions[:7]:
    force.addParticle(int(i), [])

### Fixing the backbone positions ###
backbone = file.topology.select('backbone')
backbone_list = []
for i in backbone:
    backbone_list.append(i)
for a in backbone_list:
    system.setParticleMass(int(a), 1e10)

# Barostat
system.addForce(mm.MonteCarloBarostat(1*unit.atmospheres, 298.15*unit.kelvin, 25))    

### Integrator ###
integrator = mm.LangevinIntegrator(298.15*kelvin, 1.0/unit.picoseconds, 2.0*unit.femtoseconds)
integrator.setConstraintTolerance(0.00001)

### Platform ###
platform = mm.Platform.getPlatformByName('CUDA')
properties = {'CudaPrecision': 'mixed', 'CudaDeviceIndex': '0,1'}

### Start Simulation ###
simulation = Simulation(modeller.topology, system, integrator, platform, properties)
simulation.context.setPositions(modeller.positions)


### Load checkpoint ###

# Load the checkpoint
#with open('checkpoint_1.chk', 'rb') as f:
#    simulation.context.loadCheckpoint(f.read())

### Temperature equilibration ###
simulation.context.setVelocitiesToTemperature(298.15*kelvin)
print('Equilibrating...')
simulation.step(10000)

### Reporters ####
dcd = md.reporters.DCDReporter('run.dcd', 1000, atomSubset=protein_CI)
simulation.reporters.append(dcd)

simulation.reporters.append(PDBReporter('run.pdb', 125000000))


simulation.reporters.append(app.StateDataReporter(stdout, 1000, step=True, 
    time=True, potentialEnergy=False, kineticEnergy=False, totalEnergy=True, 
    temperature=True, progress=True, 
    remainingTime=True, speed=True, totalSteps=125000000, separator='	'))

print('Running Production...')
simulation.step(125000000)

### Save checkpoint ###
with open('checkpoint_1.chk', 'wb') as f:
    f.write(simulation.context.createCheckpoint())

print('Done!')