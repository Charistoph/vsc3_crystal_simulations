from __future__ import print_function

from math import sqrt
import numpy as np
from ase import Atoms
from ase.parallel import paropen
#from gpaw import GPAW, FermiDirac, PW
from gpaw.response.df import DielectricFunction

# Plot Imports
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from ase.build import bulk
from gpaw import GPAW, PW, FermiDirac
import ase.dft.kpoints as kpoints

import os

output_folder = "bandstructure_output"
try:
    os.mkdir(output_folder)
except:
    print("output folder already created")

# Generate caf2 AB-stack structure:
atoms = Atoms(symbols='CaF2',
              pbc=np.array([True,  True,  True], dtype=bool),
              cell=np.array(
                  [
                      [3.90043757,  0.,  0.],
                      [1.95021879,  3.37787802,  0.],
                      [1.95021879,  1.12595934,  3.18469394]
                  ]),
              positions=np.array(
                  [
                      [0.,  0.,  0.],
                      [5.85065636,  3.37787802,  2.38852046],
                      [1.95021879,  1.12595934,  0.79617349]
                  ]))

# Part 2: Find ground state density and diagonalize full hamiltonian
calc = GPAW(mode=PW(500),
            kpts=(6, 6, 3),
            xc='RPBE',
            # Use smaller Fermi-Dirac smearing to avoid intraband transitions:
            occupations=FermiDirac(0.05),
            # nbands=0 will give zero empty bands,
            # nbands=-n will give n empty bands,
            # nao gives same number of bands as are atomic orbitals.
            nbands=100)

atoms.set_calculator(calc)
atoms.get_potential_energy()

# Suggested by Ask Larsen
special_points = kpoints.get_special_points(atoms.cell)
print("\nSpecial Points: ", special_points)  # decide some nice points
bandpath = 'GWUXL'
kpts, xcoords, labels = kpoints.bandpath(bandpath, atoms.cell, 100)

calc.set(kpts=kpts, fixdensity=True)
atoms.get_potential_energy()

bs = atoms.calc.band_structure()
# bs.plot(emin=-10, emax=50, filename=output_folder + '/caf2_bandstructure.png')
bs.plot(filename=output_folder + '/caf2_bandstructure.png')
bs.write(filename=output_folder + '/caf2_bandstructure.json')
