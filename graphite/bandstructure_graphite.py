from __future__ import print_function

from math import sqrt
import numpy as np
from ase import Atoms
from ase.parallel import paropen
from gpaw import GPAW, FermiDirac, PW
from gpaw.response.df import DielectricFunction

# Plot Imports
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

output_folder = "bandstructure_output"

# Part 1: Ground state calculation
a = 1.42
c = 3.355

# Generate graphite AB-stack structure:
atoms = Atoms('C4',
              scaled_positions=[(1 / 3.0, 1 / 3.0, 0),
                                (2 / 3.0, 2 / 3.0, 0),
                                (0, 0, 0.5),
                                (1 / 3.0, 1 / 3.0, 0.5)],
              pbc=(1, 1, 1),
              cell=[(sqrt(3) * a / 2, 3 / 2.0 * a, 0),
                    (-sqrt(3) * a / 2, 3 / 2.0 * a, 0),
                    (0, 0, 2 * c)])

# Part 2: Find ground state density and diagonalize full hamiltonian
calc = GPAW(mode=PW(500),
            kpts=(6, 6, 3),
            # Use smaller Fermi-Dirac smearing to avoid intraband transitions:
            occupations=FermiDirac(0.05),
            # nbands=0 will give zero empty bands, nbands=-n will give n empty bands, nao gives same number of bands as are atomic orbitals.
            nbands=40)

atoms.set_calculator(calc)
atoms.get_potential_energy()

# Suggestion from Ask Larsen
# old 'path': 'GKMGAHLG'
calc.set(kpts={'path': 'AGKMLHAGM', 'npoints': 1000},
         fixdensity=True,
         symmetry='off')
atoms.get_potential_energy()

# Part 3
bs = atoms.calc.band_structure()
# bs.plot(emin=-20, emax=50, filename=output_folder + '/bandstructure_graphite.png')
bs.plot(filename=output_folder + '/bandstructure_graphite.png')
bs.write(filename=output_folder + '/bandstructure_graphite.json')
