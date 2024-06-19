import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler

gempa = pd.read_csv("gempa.csv", delimiter=";")

#selecting attribute
gempa_x = gempa.drop(["Nomor_KK", "Nama_KK", "Alamat_Asli", "Cluster"], axis=1)

#change data into array
x_array = np.array(gempa_x)

#normalisation process
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)

#insert array to dbscans
dbscans = DBSCAN(eps=0.1, min_samples=3)
dbscans.fit(x_scaled)

#menampilkan jumlah cluster
labels=dbscans.labels_
n_raw = len(labels)
n_clusters_ =len(set(labels)) - (1 if -1 in labels else 0)
print("Terdapat "+ str(n_clusters_) + " Cluster yang terbentuk")

#show cluster data
for i in range(1, 20):
    print("longitudinal : " + str(gempa.values[i, 0]) + " latitude : " + str(gempa.values[i, 1]) + ", Cluster : " + str(dbscans.labels_[i]))
    print("-------------------------------------------------------------------------------------------------------------")

#showing data visualisation
gempa["kluster"] = dbscans.labels_
output = plt.scatter(x_scaled[:, 0], x_scaled[:, 1], s=100, c=gempa.kluster, marker="o", alpha=1,)
plt.title("Hasil Klustering k-means")
plt.colorbar(output)
plt.legend()
plt.show()
