import numpy as np
import matplotlib.pyplot as plt
import csv
# import pandas as pd


def open_eels(filename):
    f = open(filename)
    data2 = csv.reader(f, delimiter=',', quotechar='|')

    arr = []
    [arr.append(row) for row in data2]
    arr = np.array(arr[1:], dtype=float)
    arr = np.transpose(arr)
    return arr


# ==================================================================================================
# open & load Prof. Werner contact generated data
# open ASE & GPAW generated data


eels1 = open_eels("caf2_EELS_1")
eels2 = open_eels("caf2_EELS_2")
eels3 = open_eels("caf2_EELS_3")
eels4 = open_eels("caf2_EELS_4")
eels5 = open_eels("caf2_EELS_5")

# test data
for i in range(len(eels1)):
    plt.title('EELS CaF2 %s' % str(i))
    plt.plot(eels1[0], eels1[i])
    # plt.show()
    plt.xlabel("Energy [EV]")
    plt.ylabel("Loss Function")
    plt.savefig('overlays/eels_caf2_test_%s.png' % str(i))
    plt.gcf().clear()


# ==================================================================================================

# plot EELS comparison

i = 2
plt.title('EELS Overlay CaF2 Diff to 0.49 ANG')
elabel1, = plt.plot(eels1[0], eels1[i]-eels5[i], label="EELS 1")
elabel2, = plt.plot(eels2[0], eels2[i]-eels5[i], label="EELS 2")
elabel3, = plt.plot(eels3[0], eels3[i]-eels5[i], label="EELS 3")
elabel4, = plt.plot(eels4[0], eels4[i]-eels5[i], label="EELS 4")
# plt.show()
plt.xlabel("Energy [EV]")
plt.ylabel("DIFF Loss Function")
plt.legend(handles=[elabel1, elabel2, elabel3, elabel4])
plt.savefig('overlays/eels_caf2_overlay_diff_to_5_0.49.png')
plt.gcf().clear()

i = 1
plt.title('EELS Overlay CaF2')
elabel1, = plt.plot(eels1[0], eels1[i], label="EELS 1")
elabel2, = plt.plot(eels2[0], eels2[i], label="EELS 2")
elabel3, = plt.plot(eels3[0], eels3[i], label="EELS 3")
elabel4, = plt.plot(eels4[0], eels4[i], label="EELS 4")
elabel5, = plt.plot(eels5[0], eels5[i], label="EELS 5")
# plt.show()
plt.xlabel("Energy [EV]")
plt.ylabel("Loss Function")
plt.legend(handles=[elabel1, elabel2, elabel3, elabel4, elabel5])
plt.savefig('overlays/eels_caf3_overlay_eels_NLFC_w.png')
plt.gcf().clear()

i = 2
plt.title('EELS Overlay CaF2')
elabel1, = plt.plot(eels1[0], eels1[i], label="EELS 1")
elabel2, = plt.plot(eels2[0], eels2[i], label="EELS 2")
elabel3, = plt.plot(eels3[0], eels3[i], label="EELS 3")
elabel4, = plt.plot(eels4[0], eels4[i], label="EELS 4")
elabel5, = plt.plot(eels5[0], eels5[i], label="EELS 5")
# plt.show()
plt.xlabel("Energy [EV]")
plt.ylabel("Loss Function")
plt.legend(handles=[elabel1, elabel2, elabel3, elabel4, elabel5])
plt.savefig('overlays/eels_caf2_overlay_eels_LFC_w.png')
plt.gcf().clear()
