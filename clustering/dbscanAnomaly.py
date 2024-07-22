import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler

# Load data
card = pd.read_csv("CreditCardTransaction.csv", delimiter=";")

# Convert TranxDate column to TranxDatetime
card['TranxDate'] = pd.to_datetime(card['TranxDate'])

# Select attributes (excluding non-numeric columns)
card_x = card.drop(["Department", "Division", "Year", "Month", "Merchant", "TranxDescription", "TranxDate"], axis=1)

# Convert TranxDate to numeric (number of days since epoch)
card['TranxDate'] = (card['TranxDate'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
card_x['TranxDate'] = card['TranxDate']

# Change data into array
x_array = np.array(card_x)

# Normalization process
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)

# Insert array to DBSCAN
dbscans = DBSCAN(eps=0.1, min_samples=6)
dbscans.fit(x_scaled)

# Menampilkan jumlah cluster
labels = dbscans.labels_
n_raw = len(labels)
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
print("Terdapat " + str(n_clusters_) + " Cluster yang terbentuk")

a = int(input("Masukan nomor cluster yang ingin di lihat (0-" + str(n_clusters_ - 1) + ", tekan -1 jika ingin melihat data tak wajar): "))

# Show cluster data
for i in range(0, 500):
    if dbscans.labels_[i] == a:
        print("idobservasi : " + str(card.values[i, 0]) + " Nukleocapsid : " + str(card.values[i, 1]) + " Spike : " + str(card.values[i, 2]) + ", Cluster : " + str(dbscans.labels_[i]))
        print("-------------------------------------------------------------------------------------------------------------")

# Showing data visualization
card["kluster"] = dbscans.labels_
output = plt.scatter(x_scaled[:, 0], x_scaled[:, 1], s=100, c=card.kluster, marker="o", alpha=1,)
plt.title("Hasil Klustering DBSCAN")
plt.colorbar(output)
plt.legend()
plt.show()
