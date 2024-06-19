import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

# Memasukkan data set
sensus = pd.read_csv("Sink-Ship.csv", delimiter=";")
print(sensus)

# Mengonversi variabel kategorikal menjadi numerik
label_encoder_sex = LabelEncoder()
sensus['Sex'] = label_encoder_sex.fit_transform(sensus['Sex'])

label_encoder_class = LabelEncoder()
sensus['Passenger Class'] = label_encoder_class.fit_transform(sensus['Passenger Class'])

# Konversi kolom 'Age' ke numerik, ganti nilai yang tidak bisa dikonversi dengan NaN
sensus['Age'] = pd.to_numeric(sensus['Age'], errors='coerce')

# Menghapus baris yang mengandung NaN pada kolom 'Age'
sensus_cleaned = sensus.dropna(subset=['Age'])

# Penentuan variabel bebas dan terikat
X = sensus_cleaned[['Sex', 'Age', 'No of Family', 'Passenger Class']]
Y = sensus_cleaned['Survived']

# Mengoperasikan algoritma k-NN
knn = KNeighborsClassifier(n_neighbors=101)
knn.fit(X, Y)

# Input data
gender = input("Masukkan Gender (Male/Female): ").capitalize()
gender_encoded = label_encoder_sex.transform([gender])[0]  # Mengonversi input Gender menjadi numerik

age = float(input("Masukkan Umur: "))
family_count = float(input("Masukkan Jumlah Keluarga: "))

passenger_class = input("Masukkan Kelas (first/second/third): ").capitalize()
passenger_class_encoded = label_encoder_class.transform([passenger_class])[0]

pendatang = [[gender_encoded, age, family_count, passenger_class_encoded]]
print(pendatang)

# Prediksi kondisi
kondisi = knn.predict(pendatang)
if kondisi[0] == 'Yes':
    print("Premi Asuransi sebesar 200 ribu dengan kompensasi 10 Juta Rupiah")
else:
    print("Premi Asuransi sebesar 100 ribu dengan kompensasi 5 juta Rupiah")



#hitung akurasi 
#Y_prediksi = knn.predict(X.values)
#print(classification_report(Y,Y_prediksi))
