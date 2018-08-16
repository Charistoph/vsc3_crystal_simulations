from ase import Atoms

import numpy as np

images = [
    Atoms(symbols='F2Ca',
          pbc=np.array([ True,  True,  True], dtype=bool),
          cell=np.array(
      [[ 3.90043757,  0.        ,  0.        ],
       [ 1.95021879,  3.37787802,  0.        ],
       [ 1.95021879,  1.12595934,  3.18469394]]),
          positions=np.array(
      [[ 5.85065636,  3.37787802,  2.38852045],
       [ 1.95021879,  1.12595934,  0.79617348],
       [ 0.        ,  0.        ,  0.        ]])),
]