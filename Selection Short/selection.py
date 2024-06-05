def selsection_srt(s):
    n = len(s)
    for i in range (n-1):
        print(s)
        smallest = i # simpan elemen terkecil dalam variable smallest
        for j in range(i + 1,n):
            if s[j] < s[smallest]:
                smallest = j # simpan elemen terkecil dalam var samllest
        s[i], s[smallest] = s[smallest], s[i]
        
s = [50,30,40,10,20]
selsection_srt(s)
print(s)