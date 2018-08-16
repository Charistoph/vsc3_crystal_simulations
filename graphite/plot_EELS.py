import matplotlib
# VERY IMPORTANT LINE
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

output_folder = "eels_output"

plt.figure(figsize=(5, 7))
Q = np.loadtxt(output_folder + '/graphite_q_list')
for i, q in enumerate(Q):
    filename = output_folder + '/graphite_EELS_' + str(i + 1)
    d = np.loadtxt(filename, delimiter=',')
    plt.plot(d[:, 0], d[:, 2] + 0.4 * (4 - i), '-',
             label='%.2f Ang$^{-1}$' % q)

plt.xlabel('Energy [eV]')
plt.ylabel('Loss Function')
plt.title('EELS spectra of graphite: $\Gamma-\mathrm{M}$')
plt.legend(loc='best')
plt.savefig(output_folder + '/graphite_EELS.png')
plt.show()
