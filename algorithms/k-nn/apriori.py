import pandas as pd
from apyori import apriori

#operasi read file data set
store_data = pd.read_csv('store_data.csv', header=None)

#transform dataset into list
records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j])for j in range(0,20)]) 

#comad to input minimum support and confidance
a = float(input('Masukan minimum support yang di buthkan : '))
b = float(input('Masukan minimum confidance yang di buthkan : '))

#implementing apriori rules
association_rules = apriori(records, min_support = a, min_confidence = b, min_lift = 3, min_length = 2)
association_results = list(association_rules)

for item in association_results:
    pair = item[0]
    items = [x for x in pair]
    print("Rules : " + items[0] + "->" + items[1])
    
    print("Suport" + str((item[1])))
    
    print("confidence : " + str(item[2][0][2]))
    
    print("======================================")

print("banyaknya Strong Assocation rules : ", len(association_results))