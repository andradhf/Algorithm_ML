import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

gempa = pd.read_csv("gempa.csv", delimiter=";")

#selecting attribute
gempa_x = gempa.drop(["Nomor_KK", "Nama_KK", "Alamat_Asli", "Cluster"], axis=1)

#change data into array
x_array = np.array(gempa_x)

#normalisation process
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)

a = int(input("Masukan jumlah cluster yang diinginkan :"))

#insert array to kmeans
kmeans = KMeans(n_clusters=a, random_state=123)
kmeans.fit(x_scaled)

#show cluster data
for i in range(1, 20):
    print("longitudinal : " + str(gempa.values[i, 0]) + " latitude : " + str(gempa.values[i, 1]) + ", Cluster : " + str(kmeans.labels_[i]))
    print("-------------------------------------------------------------------------------------------------------------")

#showing data visualisation
gempa["kluster"] = kmeans.labels_
output = plt.scatter(x_scaled[:, 0], x_scaled[:, 1], s=100, c=gempa.kluster, marker="o", alpha=1,)
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=1, marker="s", label='Centroids')  # Plotting centroids
plt.title("Hasil Klustering k-means")
plt.colorbar(output)
plt.legend()
plt.show()
