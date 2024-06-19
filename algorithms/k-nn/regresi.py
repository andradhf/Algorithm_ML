import pandas 
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#insert data set perjalanan kapal 
df = pandas.read_csv("Sink-Ship.csv", delimiter=";")

#menentukan variable bebas
X = df[['Sex','Age','No of Family','Passenger Class']]
#menentukan variable terikat 
y = df['Survived']

#menghasilkan model regresi dari variable 
regr = LinearRegression()
regr.fit(X.values , y)
print("y= ",regr.coef_[0], "*Sex+",regr.coef_[1], "*Age+",regr.coef_[2],"*No of Family+",regr.coef_[3], "*Passenger Class+",regr.intercept_)

#data penumpang baru 
a = float(input("Masukan Gender: "))
b = float(input("Masukan Umur: "))
c = float(input("Masukan jumlah anggota keluarga: "))
d = float(input("Masukan kelas penumpang: "))

#prediksi dengan regresi linear
housePrice=[[a,b,c,d]]
price = regr.predict(housePrice)
print("Prediksi harga", price[0],"rupiah")

#visualisasi regresi 
Y_prediksi = regr.predict(X.values)

#error rms
galat = np.sqrt(np.mean(pow(Y_prediksi - y, 2)))
print("dengan perkiraan error kurang lebih: ", galat,"cc")

#plt.scatter(X,y,color='red')
#plt.scatter(X,Y_prediksi,color='blue')
#plt.title("regresi volume-co2")
#plt.xlabel("Volume")
#plt.ylabel("co2")
#plt.show()