def bubble_srt(s):
    n = len(s)
    for i in range(n):
        print(s)#untuk mengetahui proses yang terjadi 
        for j in range(n-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
s = [50,30,40,10,20]
#print('sebelum di sortir',s)
#bubble_srt(s)
#print('setelah di sort', s)

bubble_srt(s)
print(s)