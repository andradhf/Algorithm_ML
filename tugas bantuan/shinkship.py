import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
import tkinter as tk
from tkinter import messagebox

# Memasukkan data set
sensus = pd.read_csv("Sink-Ship.csv", delimiter=";")

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

# Fungsi untuk melakukan prediksi
def predict():
    try:
        gender = gender_var.get().capitalize()
        gender_encoded = label_encoder_sex.transform([gender])[0]
        
        age = float(age_var.get())
        family_count = float(family_count_var.get())
        
        passenger_class = passenger_class_var.get().capitalize()
        passenger_class_encoded = label_encoder_class.transform([passenger_class])[0]
        
        pendatang = [[gender_encoded, age, family_count, passenger_class_encoded]]
        
        kondisi = knn.predict(pendatang)
        if kondisi[0] == 'Yes':
            messagebox.showinfo("Hasil Prediksi", "Premi Asuransi sebesar 200 ribu dengan kompensasi 10 Juta Rupiah")
        else:
            messagebox.showinfo("Hasil Prediksi", "Premi Asuransi sebesar 100 ribu dengan kompensasi 5 juta Rupiah")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat interface dengan Tkinter
root = tk.Tk()
root.title("Prediksi Premi Asuransi")

tk.Label(root, text="Masukkan Gender (Male/Female):").grid(row=0, column=0)
gender_var = tk.StringVar()
tk.Entry(root, textvariable=gender_var).grid(row=0, column=1)

tk.Label(root, text="Masukkan Umur:").grid(row=1, column=0)
age_var = tk.StringVar()
tk.Entry(root, textvariable=age_var).grid(row=1, column=1)

tk.Label(root, text="Masukkan Jumlah Keluarga:").grid(row=2, column=0)
family_count_var = tk.StringVar()
tk.Entry(root, textvariable=family_count_var).grid(row=2, column=1)

tk.Label(root, text="Masukkan Kelas (first/second/third):").grid(row=3, column=0)
passenger_class_var = tk.StringVar()
tk.Entry(root, textvariable=passenger_class_var).grid(row=3, column=1)

tk.Button(root, text="Prediksi", command=predict).grid(row=4, columnspan=2)

root.mainloop()
