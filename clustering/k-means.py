import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

driver = pd.read_csv("go_track_tracks.csv")

#selecting attribute
driver_x = driver.drop(["linha", "car_or_bus", "rating_weather", "rating_bus", "rating", "time", "id", "id_android"], axis=1)

#change data into array
x_array = np.array(driver_x)

#normalisation process
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)

a = int(input("Masukan jumlah cluster yang diinginkan :"))

#insert araay to kmeans
kmeans = KMeans(n_clusters = a, random_state=123)
kmeans.fit(x_scaled)

#show cluster data
for i in range(0, 162):
    print("id record : " + str(driver.values[i,0]) + "id android : " +str(driver.values[i,1]) + ", CLuster : " + str(kmeans.labels_[i]) )
    print("-------------------------------------------------------------------------------------------------------------")

#showing data visualisation 
driver["kluster"] = kmeans.labels_
output = plt.scatter(x_scaled[:,0], x_scaled[:,1], s = 100, c = driver.kluster, marker= "o", alpha = 1,)
centers = kmeans.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c = 'red', s=200, alpha=1, marker="s");
plt.title("Hasil Klustering k-means")
plt.colorbar (output)
plt.show()
