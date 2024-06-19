import pandas as pd
from apyori import apriori


resto = pd.read_csv('./resto.csv', delimiter=";")
print(resto)

records = []
for i in range(len(resto)):
    records.append([str(resto.values[i, j]) for j in range(len(resto.columns))])

a = float(input("Masukkan Minimum Support yang Anda inginkan: "))
b = float(input("Masukkan Minimum Confidence yang Anda inginkan: "))


association_rules = apriori(records, min_support=a, min_confidence=b, min_lift=3, min_length=2)
association_result = list(association_rules)

for item in association_result:
    pair = item[0]
    items = [x for x in pair]
    print("Rules: " + items[0] + " -> " + items[1])
    print("Support: " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("=====================")

print("Banyaknya Strong Rules Assosiation Rules: ", len(association_result))