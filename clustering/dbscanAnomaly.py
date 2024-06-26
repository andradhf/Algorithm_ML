import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler

driver = pd.read_csv("go_track_tracks.csv")
print(driver)

#selecting attribute
driver_x = driver.drop(["id", "id_android", "time", "rating", "rating_bus", "rating_weather", "car_or_bus", "linha"], axis=1)

#change data into array
x_array = np.array(driver_x)

#normalisation process
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)

#insert array to dbscans
dbscans = DBSCAN(eps=0.1, min_samples=5)
dbscans.fit(x_scaled)

#menampilkan jumlah cluster
labels=dbscans.labels_
n_raw = len(labels)
n_clusters_ =len(set(labels)) - (1 if -1 in labels else 0)
print("Terdapat "+ str(n_clusters_) + " Cluster yang terbentuk")

a = int(input("Masukan nomor cluster yang ingin di lihat(0-" +str(n_clusters_ -1)+", tekna -1 jika ingin melihat data tak wajar):"))

#show cluster data
for i in range(0, n_raw):
    if(dbscans.labels_[i]==a):
        print("id records : " + str(driver.values[i, 0]) + " id Androdi : " + str(driver.values[i, 1]) + ", Cluster : " + str(dbscans.labels_[i]))
        print("-------------------------------------------------------------------------------------------------------------")

#showing data visualisation
driver["kluster"] = dbscans.labels_
output = plt.scatter(x_scaled[:, 0], x_scaled[:, 1], s=100, c=driver.kluster, marker="o", alpha=1,)
plt.title("Hasil Klustering DBscans")
plt.colorbar(output)
plt.legend()
plt.show()
