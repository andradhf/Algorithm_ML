import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn.preprocessing import MinMaxScaler

# Load data
card = pd.read_csv("CreditCardTransaction.csv", delimiter=";")

# Convert TranxDate column to datetime
card['TranxDate'] = pd.to_datetime(card['TranxDate'])

# Select attributes (excluding non-numeric columns)
card_x = card.drop(["Department", "Division", "Year", "Month", "Merchant", "TranxDescription", "TranxDate"], axis=1)

# Convert TranxDate to numeric (number of days since epoch)
card['TranxDate'] = (card['TranxDate'] - pd.Timestamp("1970-01-01")) // pd.Timedelta('1s')
card_x['TranxDate'] = card['TranxDate']

# Use a subset of the data (e.g., 50,000 rows for testing)
card_x_sample = card_x.sample(n=50000, random_state=42)
x_array = np.array(card_x_sample)

# Normalization process
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x_array)

# Set initial DBSCAN parameters
eps = 0.1  # Start with a smaller value of eps
min_samples = 10  # Start with a larger value of min_samples

# Insert array to DBSCAN
dbscans = DBSCAN(eps=eps, min_samples=min_samples)
dbscans.fit(x_scaled)

# Menampilkan jumlah cluster
labels = dbscans.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_outliers = list(labels).count(-1)
print("Terdapat " + str(n_clusters_) + " cluster yang terbentuk")
print("Jumlah transaksi tidak wajar (cluster -1): " + str(n_outliers))

# Show outlier data
print("\nAnggota dari cluster -1 (outliers):")
for i in range(0, len(card_x_sample)):
    if dbscans.labels_[i] == -1:
        print("idobservasi : " + str(card.values[i, 0]) + " Nukleocapsid : " + str(card.values[i, 1]) + " Spike : " + str(card.values[i, 2]) + ", Cluster : " + str(dbscans.labels_[i]))
        print("-------------------------------------------------------------------------------------------------------------")

# Ask user if they want to see the visualization
user_input = input("\nApakah Anda ingin menampilkan visualisasi data? (y/n): ").strip().lower()

if user_input == 'y':
    # Showing data visualization
    card_x_sample["kluster"] = dbscans.labels_
    output = plt.scatter(x_scaled[:, 0], x_scaled[:, 1], s=100, c=card_x_sample.kluster, marker="o", alpha=1,)
    plt.title("Hasil Klustering DBSCAN")
    plt.colorbar(output)
    plt.show()
else:
    print("Selesai.")
