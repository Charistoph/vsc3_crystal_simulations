import matplotlib
# VERY IMPORTANT LINE
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(5, 7))
Q = np.loadtxt('caf2_q_list')
for i, q in enumerate(Q):
    filename = 'eels_output/caf2_EELS_' + str(i + 1)
    d = np.loadtxt(filename, delimiter=',')
    plt.plot(d[:, 0], d[:, 2] + 0.4 * (4 - i), '-',
             label='%.2f Ang$^{-1}$' % q)

plt.xlabel('Energy [eV]')
plt.ylabel('Loss Function')
plt.title('EELS spectra of CaF2: $\Gamma-\mathrm{M}$')
plt.legend(loc='best')
plt.savefig('eels_output/caf2_EELS.png')
plt.show()
