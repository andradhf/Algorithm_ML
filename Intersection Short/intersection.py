def intersection_srt(s):
    n = len(s)
    for i in range(1,n):
        print(s)
        x = s[i]
        j = i-1
        while j >= 0 and s[j] > x:
            s[j+1] = s[j]
            j -= 1
        s[j+1] = x
s = [50,30,40,10,20]
print("Sebelum di sortir", s)
intersection_srt(s)
print("Setelah di sortir", s)