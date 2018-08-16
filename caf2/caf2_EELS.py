"""
Electronic Loss Spectrum CaF2
"""

from __future__ import print_function

from math import sqrt
import numpy as np
from ase import Atoms
from ase.parallel import paropen
from gpaw import GPAW, FermiDirac, PW
from gpaw.response.df import DielectricFunction

output_folder = "eels_output"

# Part 1: Ground state calculation

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
            nbands=16,
            kpts=(6, 6, 3),
            # Use smaller Fermi-Dirac smearing to avoid intraband transitions:
            occupations=FermiDirac(0.05))

atoms.set_calculator(calc)
atoms.get_potential_energy()

calc.set(kpts=(20, 20, 7), fixdensity=True)
# atoms.get_potential_energy()

# The result should also be converged with respect to bands:
calc.diagonalize_full_hamiltonian(nbands=60)
calc.write('caf2.gpw', 'all')

# Part 2: Spectra calculations
f = paropen(output_folder + '/caf2_q_list', 'w')  # write q

for i in range(1, 6):  # loop over different q
    df = DielectricFunction(calc='caf2.gpw',
                            domega0=0.01,
                            eta=0.2,  # Broadening parameter.
                            ecut=100,
                            # write different output for different q:
                            txt='%s/out_df_%d.txt' % (output_folder, i))

    q_c = [i / 20.0, 0.0, 0.0]  # Gamma - M excitation

    df.get_eels_spectrum(
        q_c=q_c, filename='%s/caf2_EELS_%d' % (output_folder, i))

    # Calculate cartesian momentum vector:
    cell_cv = atoms.get_cell()
    bcell_cv = 2 * np.pi * np.linalg.inv(cell_cv).T
    q_v = np.dot(q_c, bcell_cv)
    print(sqrt(np.inner(q_v, q_v)), file=f)

f.close()
