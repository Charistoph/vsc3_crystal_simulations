import json
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

# ==================================================================================================
# functions

# NO FUNCTIONS


# ==================================================================================================
# main

# ==================================================================================================
# data load

# open & load ASE & GPAW generated data
f = open("bandstructure_graphite_nao_no_limit.json")
data = json.load(f)
f.close()
# print(data.keys())

# format data as np array & transpose
eng = np.array(data['energies'][0])
engT = np.transpose(eng)
kpts = np.array(data['kpts'])
kptsT = np.transpose(kpts)

# open & load Prof. Werner contact generated data
f = open("graphitebands_latest_Prof_Werner.csv")
data2 = csv.reader(f, delimiter=';', quotechar='|')

# format data as np array & transpose
arr = []
[arr.append(row) for row in data2]

arr = [[item.replace(',', '.') for item in elem] for elem in arr]
arr = np.array(arr[2:])
arrT = np.transpose(arr)

kptsPW = arrT[1]
engPW = arrT[2:]
kptsPW = kptsPW.astype(np.float)
energyPW = engPW.astype(np.float)


# ==================================================================================================
# **** What is what? ****
# kptsT - x-Axis of ASE/GPAW data
# engT - bands of ASE/GPAW data
# kptsPW - x-Axis of Prof. Werner data
# energyPW - bands b of Prof. Werner data


# ==================================================================================================
# manipulate data to make it comparable.

# Replace kptsT which are 3 dimensional points in k-Space
# by an set of points which linearly get bigger:
# (kptsT[i] = k*i), k = max(kptsPW)/length(engT), length(engT) == length(kptsT)
kptsT = np.zeros(len(engT[0]))
for i in range(len(kptsT)):
    kptsT[i] = i*max(kptsPW)/(len(engT[0])-1)


# ==================================================================================================
# plots

ref_value = 6.027083077932045
# ref_value = 5.9

# plot kpts
for curr in range(1, 50):
    try:
        plt.figure('band_comparison_nr_' + str(curr))
        band1, = plt.plot(kptsT, engT[curr]-ref_value, "red", label="ASE/GPAW")
        band2, = plt.plot(kptsPW, energyPW[curr], label="PW")
        # plt.show()
        plt.xlabel("")
        plt.ylabel("Energy [EV]")
        plt.legend(handles=[band1, band2])
        plt.savefig('output/band_comparison_new_nr_' +
                    str(curr) + '.png')
        plt.gcf().clear()
        plt.close()
        print("fig %d plotted" % curr)
    except:
        plt.close()
        print("band %d not plotted, maybe less than %d bands" % (curr, curr))

# ==================================================================================================
# export ASE/GPAW data to csv using pandas

total_data = np.concatenate([kpts, eng], axis=1)
df = pd.DataFrame(total_data)
df.to_csv("graphite_bandstructure_ASE_GPAW.csv", sep=';')
print("\n\nGraphite Bandstructure ASE/GPAW saved to csv\n")
